# Trabalho de AD

## Simulação -  Caches com perdas e atrasos

## Requisitos

* Python 3
    * termcolor
    * numpy
    * scipy
    * matplotlib
    * pylab
    * multiprocessing (padrão)
    * time (padrão)
    * argparse (padrão)
    * traceback (padrão)
    * math (padrão)

## Uso

Na raiz do projeto digite

```cmd
python trabalho_final.py -r=[requests] -m=[means] -c=[config] -d=[debug] 
```

Onde:  
* [requests] é um valor inteiro para o número de requisições a serem simuladas por batch.

* [means] é o número de batchs a serem realizados para obter as médias

* [config] é o nome do arquivo da pasta configs a ser utilizado como cenário pre-configurado da simulação. Este parâmetro não deve conter o path nem a extensão do arquivo, mas apenas seu nome.

* [debug] é o nível de debug a ser realizado dentre os valores abaixo. O valor padrão é (`SUCCESS`).

`NO_DEBUG`: Não mostra nada no terminal a não ser o resultado final.  
`ERROR`: Mostra apenas erros no terminal  
`WARN`: Mostra erros e warnings  
`SUCCESS`: Mostra os anteriores e Sucessos  
`INFO`: Mostra os anteriores e Informações  
`DEBUG`: Mostra os anteriores e dados de Debug


### JSON de config
O Json de config é um arquivo presente na pasta configs e que seu nome é passado como parâmetro do programa. Na pasta de configs existem muitos cenários pre-definidos para serem usados, mas é possível criar um novo apenas observando o que cada uma das configurações significam.

Configuração            | tipo          | Descrição
---------               | ------        | ----------
DataTypes               | string        | Tipos de dados a serem coletados (Possíveis valores abaixo)
Client2CacheRate        | number/string | Taxa entre cliente e cache (mi)
Client2CacheP           | number/string | Probabilidade de sucesso da requisição para a cache (P)
TimeoutRate             | number/string | Taxa de atribuição dos timeouts (alpha)
Cache2Server2CacheRate  | number/string | Taxa entre cache e servidor indo e voltando (theta)
AlternativeServerRate   | number/string | Taxa entre cliente e servidor alternativo (gamma)
UserRequestRate         | number/string | Taxa de requisições do usuário (lambda)
ContentSize             | number/string | Numero de conteúdos diferentes (N)
Caches                  | array         | Array contendo array com pares ("tipo da cache", tamanho da cache)

> Todas as taxas e a probabilidade P assumem valores entre 0 e infinito, mas para uma taxa infinita deve-se colocar a string `inf`.

Valores de **DataTypes**:

* `cache_hits`: coletar a contagem de cache hit de cada request 
* `delays`: coletar a demora de cada request
* `init_timestamps`: coletar o tempo de inicio de cada request
* `end_timestamps`: coletar o tempo de finalização de cada request

Valores de **tipos de cache**:

* `fifo`: coletar a contagem de cache hit de cada request 
* `lru`: coletar a demora de cada request
* `static`: coletar o tempo de inicio de cada request
* `random`: coletar o tempo de finalização de cada request

#### Exemplo de configuração:
Cenário 1 - FIFO - 3 conteúdos
```json
{
    "DataTypes": "cache_hits",
    "Client2CacheRate": "inf",
    "Client2CacheP": 1,
    "TimeoutRate": 0,
    "Cache2Server2CacheRate": "inf",
    "AlternativeServerRate": 1,
    "UserRequestRate" : 1,
    "ContentSize" : 3,
    "Caches" : [
        ["fifo", 2],
        ["fifo", 2]
    ]
}
```