import traceback
import aiohttp
from django.http import HttpResponse
from django.shortcuts import render
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
import nest_asyncio
import os
import logging
import plotly.express as px

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_file():
    download_directory = "/Users/andrenunes/PycharmProjects/POS_PYTHON/downloads"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executar em modo headless
    options.add_argument("--disable-gpu")  # Desabilitar GPU (recomendado no modo headless)
    options.add_argument("--no-sandbox")  # Desabilitar o sandbox (necessário em alguns sistemas)
    options.add_argument("--disable-dev-shm-usage")  # Superar problemas de recursos compartilhados
    prefs = {"download.default_directory": download_directory}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")
    btn_download = driver.find_element(By.PARTIAL_LINK_TEXT, "Download")
    btn_download.click()
    logging.info("Download iniciado...")
    time.sleep(10)  # Aumente o tempo de espera se necessário para garantir que o download seja concluído
    driver.close()
    logging.info("Download concluído e navegador fechado.")


def get_latest_file(directory):
    files = os.listdir(directory)
    paths = [os.path.join(directory, basename) for basename in files if basename.startswith("IBOVDia")]
    latest_file = max(paths, key=os.path.getctime)
    logging.info(f"Arquivo mais recente encontrado: {latest_file}")
    return latest_file


def get_symbols():
    get_file()
    download_directory = "/Users/andrenunes/PycharmProjects/POS_PYTHON/downloads"
    nome_arquivo = get_latest_file(download_directory)

    if not os.path.exists(nome_arquivo):
        logging.error(f"Arquivo {nome_arquivo} não encontrado.")
        raise FileNotFoundError(f"Arquivo {nome_arquivo} não encontrado.")

    with open(nome_arquivo, 'r', encoding='iso-8859-1') as arquivo:
        linhas = arquivo.readlines()
        nomes_alterados = [linha.split(';')[0] + ".SA" for linha in linhas[2:-2]]
    logging.info(f"Símbolos extraídos: {nomes_alterados}")
    return nomes_alterados


async def fetch_single_stock_data(symbol, start_date, end_date):
    df = yf.Ticker(symbol).history(start=start_date, end=end_date)['Close']
  #  await asyncio.sleep(1)  # Simula um atraso para garantir comportamento assíncrono
    df = df.ffill().bfill()  # Preenche NaNs com o primeiro e último valor válido
    return symbol, df


async def fetch_stock_data(symbols, months):
    logging.info("Iniciando fetch_stock_data")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months * 30)
    all_data = {}

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_single_stock_data(symbol, start_date, end_date)) for symbol in symbols]
        results = await asyncio.gather(*tasks)

    for symbol, df in results:
        all_data[symbol] = df

    combined_df = pd.DataFrame(all_data)
    combined_df.index.name = 'Date'
    logging.info("fetch_stock_data concluído")
    return combined_df


def calculate_rentability(df):
    rentability_data = [
        (symbol, (df[symbol].iloc[-1] - df[symbol].iloc[0]) / df[symbol].iloc[0])
        for symbol in df.columns]
    rentability_df = pd.DataFrame(rentability_data, columns=['Empresa', 'Rentability'])
    rentability_df.sort_values('Rentability', ascending=False, inplace=True)
    top_stocks = rentability_df.head(10)
    logging.info(f"Rentabilidade Top 10 calculada")
    return top_stocks


def index(request):
    if request.method == 'POST':
        try:
            logging.info("View 'index' chamada")
            months = int(request.POST.get('months', 4))  # Valor padrão é 4 meses
            logging.info(f"Meses selecionados: {months}")
            symbols = get_symbols()
            logging.info(f"Símbolos obtidos: {symbols}")
            nest_asyncio.apply()
            logging.info("Aplicando nest_asyncio")
            df = asyncio.run(fetch_stock_data(symbols, months))
            logging.info("Dados das ações obtidos")
            rentability_df = calculate_rentability(df)
            rentability_df.sort_values('Rentability', ascending=False, inplace=True)
            top_stocks = rentability_df.head(10)

            fig = px.bar(top_stocks, x='Empresa', y='Rentability',
                         title=f'Top 10 Ações Mais Rentáveis dos Últimos {months} Meses',
                         labels={'Rentability': 'Valorização', 'Empresa': 'Ações'})

            graph_html = fig.to_html(full_html=False)
            table_html = top_stocks.to_html(classes='table table-striped text-center', index=False)

            logging.info("Renderizando template com gráficos")
            return HttpResponse(graph_html + table_html)
        except FileNotFoundError as e:
            logging.error(str(e))
            return HttpResponse(f"Erro: {str(e)}", status=400)
        except Exception as e:
            logging.error(f"Erro inesperado: {str(e)}")
            logging.error(traceback.format_exc())
            return HttpResponse(f"Erro inesperado: {str(e)}", status=500)
    else:
        return render(request, 'stocks/index.html',
                      {'months': 4, 'graph_html': '', 'months_range': range(1, 13), 'table_html': ''})
