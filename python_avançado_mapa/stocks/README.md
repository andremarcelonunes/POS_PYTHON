
# Top 10 Ações Mais Rentáveis

Este projeto é uma aplicação web que exibe as 10 ações mais rentáveis dos últimos meses, utilizando dados da B3 e Yahoo Finance. A aplicação é construída com Django, Bootstrap para a interface, e utiliza AJAX para uma experiência de usuário interativa e responsiva.

## Funcionalidades

- **Selecionar período**: Permite selecionar a quantidade de meses para a consulta de dados.
- **Gráfico dinâmico**: Exibe um gráfico interativo das ações mais rentáveis.
- **Tabela de dados**: Mostra uma tabela com as ações e suas respectivas rentabilidades.
- **Atualização dinâmica**: Utiliza AJAX para atualizar os dados sem recarregar a página.

## Tecnologias Utilizadas

- **Django**: Framework web para o backend.
- **Bootstrap**: Framework CSS para a interface responsiva.
- **AJAX**: Para submissão assíncrona do formulário.
- **yfinance**: Biblioteca para obter dados históricos das ações.
- **aiohttp**: Biblioteca para requisições assíncronas.
- **pandas**: Biblioteca para manipulação de dados.
- **Plotly**: Biblioteca para geração de gráficos interativos.

## Como Executar

### Pré-requisitos

- Python 3.x
- pip

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Configuração

Certifique-se de ter o ChromeDriver instalado e configurado no seu PATH.

### Execução

1. Aplique as migrações do Django:

   ```bash
   python manage.py migrate
   ```

2. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

3. Acesse a aplicação em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Referências

- **CLARK, Fredrik et al.** Pillow. Disponível em: [https://pillow.readthedocs.io/en/stable/](https://pillow.readthedocs.io/en/stable/). Acesso em: 1 maio 2024.
- **BRADSKI, Gary; KAEHLER, Adrian.** OpenCV. Disponível em: [https://opencv.org](https://opencv.org). Acesso em: 2 maio 2024.
- **LUNDE, Mark.** Tkinter. Disponível em: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html). Acesso em: 2 maio 2024.
- **Django Project.** Django. Disponível em: [https://www.djangoproject.com/](https://www.djangoproject.com/). Acesso em: 2 maio 2024.
- **Yahoo Finance.** yfinance. Disponível em: [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/). Acesso em: 2 maio 2024.
- **PANDAS Development Team.** pandas. Disponível em: [https://pandas.pydata.org/](https://pandas.pydata.org/). Acesso em: 2 maio 2024.
- **aio-libs.** aiohttp. Disponível em: [https://docs.aiohttp.org/en/stable/](https://docs.aiohttp.org/en/stable/). Acesso em: 2 maio 2024.
- **NEST_ASYNCIO.** nest_asyncio. Disponível em: [https://pypi.org/project/nest-asyncio/](https://pypi.org/project/nest-asyncio/). Acesso em: 2 maio 2024.
- **Plotly.** plotly. Disponível em: [https://plotly.com/python/](https://plotly.com/python/). Acesso em: 2 maio 2024.

## Contribuição

1. Fork o projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
