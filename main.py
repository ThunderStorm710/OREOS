import numpy as np
import re
import matplotlib.pyplot as plt
from scipy import stats

# Define regular expressions for extracting relevant information
pod_results_pattern = re.compile(r'Pod Results(.+?)Pod Creation Success Rate: ([\d.]+) %', re.DOTALL)
deployment_results_pattern = re.compile(r'Deployment Results(.+?)Pod Creation Success Rate: ([\d.]+) %', re.DOTALL)
namespace_results_pattern = re.compile(r'Namespace Results(.+?)Service API Call Latencies \(ms\)', re.DOTALL)
namespace_results_pattern1 = re.compile(r'Namespace Results(.+?)Benchmark run completed.', re.DOTALL)
service_results_pattern = re.compile(r'Service Results(.+?)Benchmark run completed.', re.DOTALL)

ficheiros = ["cp_light_1client", "cp_light_4client", "cp_heavy_8client", "cp_heavy_12client"]

pods = {
    'Pod Creation Throughput': [],
    'Pod Client-Server E2E Latency': [],
    'Pod Scheduling Latency Stats': [],
    'Pod Initialization Latency (Kubelet)': [],
    'Pod Starting Latency Stats': [],
    'Pod Creation Avg Latency': [],
    'Pod Startup Total Latency': [],
}
pod_api = {

    "Delete Latency": [],
    "Create Latency": [],
    "List Latency": [],
    "Get Latency": [],
    "Update Latency": []
}
service_api = {

    "Delete Latency": [],
    "Create Latency": [],
    "List Latency": [],
    "Get Latency": [],
    "Update Latency": []
}

deployment_api = {

    "Delete Latency": [],
    "Create Latency": [],
    "List Latency": [],
    "Get Latency": [],
    "Update Latency": []
}

namespace_api = {

    "Delete Latency": [],
    "Create Latency": [],
    "List Latency": [],
    "Get Latency": [],
    "Update Latency": []
}
deployments = {
    'Pod Creation Throughput': [],
    'Pod Client-Server E2E Latency': [],
    'Pod Scheduling Latency Stats': [],
    'Pod Initialization Latency (Kubelet)': [],
    'Pod Starting Latency Stats': [],
    'Pod Creation Avg Latency': [],
    'Pod Startup Total Latency': [],
}
light_1 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
           'service_api': service_api.copy(),
           'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}
light_4 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
           'service_api': service_api.copy(),
           'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}
heavy_8 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
           'service_api': service_api.copy(),
           'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}
heavy_12 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
            'service_api': service_api.copy(),
            'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}

k0sGlobal = [light_1.copy(), light_4.copy(), heavy_8.copy(), heavy_12.copy()]
k3sGlobal = [light_1.copy(), light_4.copy(), heavy_8.copy(), heavy_12.copy()]
k8sGlobal = [light_1.copy(), light_4.copy(), heavy_8.copy(), heavy_12.copy()]


# Function to extract and print the relevant information
def extract_results(log_content):
    pod_results_match = pod_results_pattern.search(log_content)
    deployment_results_match = deployment_results_pattern.search(log_content)
    namespace_results_match = namespace_results_pattern.search(log_content)
    namespace_results_match1 = namespace_results_pattern1.search(log_content)
    service_results_match = service_results_pattern.search(log_content)

    if pod_results_match:
        pod_results_content = pod_results_match.group(1).strip()
        pod_success_rate = pod_results_match.group(2).strip()
        # print("Pod Results:")
        # print(pod_results_content)
        lista = pod_results_content.split("\n")
        for i in lista:
            if "Pod creation throughput (pods/minutes):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                # print(float(linha[6]))
                pods['Pod Creation Throughput'].append(float(linha[6]))

            elif "Pod creation average latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                # print(float(linha[6]))
                pods['Pod Creation Avg Latency'].append(float(linha[6]))

            elif "Pod startup total latency (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Startup Total Latency'].append(l)

            elif "Pod client-server e2e latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Client-Server E2E Latency'].append(l)

            elif "Pod scheduling latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Scheduling Latency Stats'].append(l)

            elif "Pod initialization latency on kubelet (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Initialization Latency (Kubelet)'].append(l)

            elif "Pod starting latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Starting Latency Stats'].append(l)


            elif "delete pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Delete Latency'].append(l)
            elif "create pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Create Latency'].append(l)
            elif "list pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['List Latency'].append(l)
            elif "get pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Get Latency'].append(l)
            elif "update pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Update Latency'].append(l)

        print(f"Pod Success Rate: {pod_success_rate}%")

    if deployment_results_match:
        deployment_results_content = deployment_results_match.group(1).strip()
        deployment_success_rate = deployment_results_match.group(2).strip()
        # print("\nDeployment Results:")
        # print(deployment_results_content)
        print(f"Deployment Success Rate: {deployment_success_rate}%")

        lista = deployment_results_content.split("\n")
        for i in lista:
            if "Pod creation throughput (pods/minutes):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                # print(float(linha[6]))
                deployments['Pod Creation Throughput'].append(float(linha[6]))

            elif "Pod creation average latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                # print(float(linha[6]))
                deployments['Pod Creation Avg Latency'].append(float(linha[6]))

            elif "Pod startup total latency (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Startup Total Latency'].append(l)

            elif "Pod client-server e2e latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Client-Server E2E Latency'].append(l)

            elif "Pod scheduling latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Scheduling Latency Stats'].append(l)

            elif "Pod initialization latency on kubelet (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Initialization Latency (Kubelet)'].append(l)

            elif "Pod starting latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Starting Latency Stats'].append(l)


            elif "delete deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Delete Latency'].append(l)
            elif "create deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Create Latency'].append(l)
            elif "list deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['List Latency'].append(l)
            elif "get deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Get Latency'].append(l)
            elif "update deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Update Latency'].append(l)

    if namespace_results_match or namespace_results_match1:
        if namespace_results_match:
            namespace_results_content = namespace_results_match.group(1).strip()
        else:
            namespace_results_content = namespace_results_match1.group(1).strip()

        # print("\nNamespace Results:")
        lista = namespace_results_content.split("\n")
        for i in lista:
            if "delete namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Delete Latency'].append(l)
            elif "create namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Create Latency'].append(l)
            elif "list namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['List Latency'].append(l)
            elif "get namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Get Latency'].append(l)
            elif "update namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Update Latency'].append(l)

    if service_results_match:
        service_results_content = service_results_match.group(1).strip()
        # print("\nService Results:")
        # print(service_results_content)
        lista = service_results_content.split("\n")
        for i in lista:
            if "delete service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Delete Latency'].append(l)
            elif "create service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Create Latency'].append(l)
            elif "list service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['List Latency'].append(l)
            elif "get service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Get Latency'].append(l)
            elif "update service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Update Latency'].append(l)


# Função para calcular o intervalo de confiança
def calcular_intervalo_confianca(dados, alpha):
    media = np.mean(dados)
    desvio_padrao = np.std(dados, ddof=1)  # Usar ddof=1 para calcular o desvio padrão amostral
    tamanho_amostra = len(dados)
    t_valor = stats.t.ppf(1 - alpha / 2, tamanho_amostra - 1)  # Valor crítico da distribuição t de Student

    margem_erro = t_valor * (desvio_padrao / np.sqrt(tamanho_amostra))

    intervalo_inferior = media - margem_erro
    intervalo_superior = media + margem_erro

    return intervalo_inferior, intervalo_superior


def calcular_estatisticas_das_listas(listas):
    estatisticas = {}

    for nome, lista in listas.items():

        if isinstance(lista[0], list):
            lista_transposta = np.array(lista).T
            print(lista_transposta)
            medias = [np.mean(sublista) for sublista in lista_transposta]
            minI = [-1 for _ in range(4)]
            maxI = [-1 for _ in range(4)]
            for i in range(len(lista_transposta)):
                minI[i], maxI[i] = calcular_intervalo_confianca(lista_transposta[i], 0.05)

            estatisticas[nome] = {
                'Mediana': [minI[0], medias[0], maxI[0]],
                'Mínimo': [minI[1], medias[1], maxI[1]],
                'Máximo': [minI[2], medias[2], maxI[2]],
            }


        else:
            minI, maxI = calcular_intervalo_confianca(lista, 0.05)

            # Listas simples - calcular estatísticas diretas
            medianas = np.mean(lista)
            minimos = np.mean(lista)
            maximos = np.mean(lista)

            estatisticas[nome] = {
                'Mediana': [minI, medianas, maxI],
                'Mínimo': [minI, minimos, maxI],
                'Máximo': [minI, maximos, maxI],
            }

    return estatisticas


def criar_grafico_de_barras(valoresk3s, valoresk8s, valoresk0s, titulo: str, ficheiro):
    plataformas = ['Minimum', 'Median', 'Maximum']
    k3s = [valoresk3s['Mínimo'][1], valoresk3s['Mediana'][1], valoresk3s['Máximo'][1]]
    k8s = [valoresk8s['Mínimo'][1], valoresk8s['Mediana'][1], valoresk8s['Máximo'][1]]
    k0s = [valoresk0s['Mínimo'][1], valoresk0s['Mediana'][1], valoresk0s['Máximo'][1]]

    ic_k3s = [(valoresk3s['Mínimo'][2] - valoresk3s['Mínimo'][0]) / 2,
              (valoresk3s['Mediana'][2] - valoresk3s['Mediana'][0]) / 2,
              (valoresk3s['Máximo'][2] - valoresk3s['Máximo'][0]) / 2]
    ic_k8s = [(valoresk8s['Mínimo'][2] - valoresk8s['Mínimo'][0]) / 2,
              (valoresk8s['Mediana'][2] - valoresk8s['Mediana'][0]) / 2,
              (valoresk8s['Máximo'][2] - valoresk8s['Máximo'][0]) / 2]
    ic_k0s = [(valoresk0s['Mínimo'][2] - valoresk0s['Mínimo'][0]) / 2,
              (valoresk0s['Mediana'][2] - valoresk0s['Mediana'][0]) / 2,
              (valoresk0s['Máximo'][2] - valoresk0s['Máximo'][0]) / 2]
    # Configura a largura das barras
    largura = 0.2

    posicoes = range(len(plataformas))

    plt.bar([p - largura for p in posicoes], k0s, width=largura, label='k0s', color='green', yerr=ic_k0s, capsize=5)
    plt.bar(posicoes, k3s, width=largura, label='k3s', color='blue', yerr=ic_k3s, capsize=5)
    plt.bar([p + largura for p in posicoes], k8s, width=largura, label='k8s', color='orange', yerr=ic_k8s, capsize=5)
    plt.grid("on")
    # plt.title(titulo)

    plt.xticks(posicoes, plataformas)
    # plt.xlabel("Mínimo, Mediana e Máximo de cada distribuição")
    if not "Throughput" in titulo:
        plt.ylabel("Time (ms)")
    else:
        plt.ylabel("Number of pods per second")

    plt.tight_layout(rect=[0, 0, 1, 0.85])
    plt.legend(['k0s', 'k3s', 'k8s'], bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
               borderaxespad=0, ncol=3)
    titulo = titulo.replace(" ", "")
    titulo = titulo.replace(">", "")
    file = f"{titulo}-{ficheiro}.png"
    plt.savefig(file)
    plt.show()


def criar_grafico_de_barras_separados(valoresk0s, valoresk3s, valoresk8s, titulo):
    grupos_grandes = ['1 client', '4 clients', '8 clients', '12 clients']
    subgrupos = ['Mínimo', 'Mediana', 'Máximo']
    nomes = ['Minimum', 'Median', 'Maximum']

    cores_k0s = ['blue', 'red', 'purple']
    cores_k3s = ['green', 'orange', 'magenta']
    cores_k8s = ['cyan', 'yellow', 'pink']
    cores = ['blue', 'green', 'orange']

    largura = 0.1
    espaco_entre_grupos = 0.3

    if titulo == "Pod Creation Throughput" or titulo == "Pod Creation Avg Latency":
        espaco_entre_grupos = 0.2

        total_largura = largura + espaco_entre_grupos
        indices_grandes = np.arange(len(grupos_grandes)) * (total_largura + espaco_entre_grupos)

        fig, ax = plt.subplots(figsize=(12, 6))

        for i, grupo in enumerate(grupos_grandes):
            posicao_grupo = indices_grandes[i]

            valor_k0s = valoresk0s[i]['pods'][titulo]['Mediana'][1]
            ic_k0s = (valoresk0s[i]['pods'][titulo]['Mediana'][2] - valoresk0s[i]['pods'][titulo]['Mediana'][0]) / 2
            ax.bar(posicao_grupo, valor_k0s, largura, yerr=ic_k0s, label='k0s', color=cores, capsize=2, hatch="/")

            valor_k3s = valoresk3s[i]['pods'][titulo]['Mediana'][1]
            ic_k3s = (valoresk3s[i]['pods'][titulo]['Mediana'][2] - valoresk3s[i]['pods'][titulo]['Mediana'][0]) / 2
            ax.bar(posicao_grupo + largura, valor_k3s, largura, yerr=ic_k3s, label='k3s', color=cores, capsize=2, hatch="|")

            valor_k8s = valoresk8s[i]['pods'][titulo]['Mediana'][1]
            ic_k8s = (valoresk8s[i]['pods'][titulo]['Mediana'][2] - valoresk8s[i]['pods'][titulo]['Mediana'][0]) / 2
            ax.bar(posicao_grupo + largura * 2, valor_k8s, largura, yerr=ic_k8s, label='k8s', color=cores, capsize=2, hatch="-")

        ax.set_xticks(indices_grandes + 0.1)
        ax.set_xticklabels(grupos_grandes, fontsize=14)
        ax.set_ylabel("Throughput (pods/minutes)", fontsize=14)

        plt.grid(True)
        plt.legend(['k0s', 'k3s', 'k8s'], bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
                   borderaxespad=0, ncol=3, fontsize=14)
        plt.tight_layout(rect=[0, 0, 1, 1])
        plt.grid(True)

        # Salva e mostra o gráfico
        plt.savefig(f'{titulo}.png')
        plt.show()
    else:

        num_subgrupos = len(subgrupos)
        total_largura = (num_subgrupos * largura) + ((num_subgrupos - 1) * espaco_entre_grupos)
        indices_grandes = np.arange(len(grupos_grandes)) * (total_largura + 2 * espaco_entre_grupos)

        fig, ax = plt.subplots(figsize=(15, 6))

        # Desenhar as barras para cada plataforma
        for i, subgrupo in enumerate(subgrupos):
            posicoes = indices_grandes + (i * (largura + espaco_entre_grupos))

            valores_k0s = [valoresk0s[grupo]['pods'][titulo][subgrupo][1] for grupo in
                           range(len(grupos_grandes))]
            print(valoresk0s[0]['pods'][titulo])
            print(valoresk0s[0]['pods'][titulo]['Mediana'][0])
            print(valoresk0s[0]['pods'][titulo]['Mediana'][1])
            print(valoresk0s[0]['pods'][titulo]['Mediana'][2])
            ic_k0s = [(valoresk0s[grupo]['pods'][titulo][subgrupo][2] -
                       valoresk0s[grupo]['pods'][titulo][subgrupo][0]) / 2 for grupo in
                      range(len(grupos_grandes))]
            ax.bar(posicoes, valores_k0s, largura, yerr=ic_k0s, label=f'k0s - {nomes[i]}', color=cores_k0s[i],
                   capsize=2, hatch="-")

            valores_k3s = [valoresk3s[grupo]['pods'][titulo][subgrupo][1] for grupo in
                           range(len(grupos_grandes))]
            ic_k3s = [(valoresk3s[grupo]['pods'][titulo][subgrupo][2] -
                       valoresk3s[grupo]['pods'][titulo][subgrupo][0]) / 2 for grupo in
                      range(len(grupos_grandes))]
            ax.bar(posicoes + largura, valores_k3s, largura, yerr=ic_k3s, label=f'k3s - {nomes[i]} ',
                   color=cores_k3s[i],
                   capsize=2, hatch="-")

            valores_k8s = [valoresk8s[grupo]['pods'][titulo][subgrupo][1] for grupo in
                           range(len(grupos_grandes))]
            ic_k8s = [(valoresk8s[grupo]['pods'][titulo][subgrupo][2] -
                       valoresk8s[grupo]['pods'][titulo][subgrupo][0]) / 2 for grupo in
                      range(len(grupos_grandes))]
            ax.bar(posicoes + largura * 2, valores_k8s, largura, yerr=ic_k8s, label=f'k8s - {nomes[i]}',
                   color=cores_k8s[i],
                   capsize=2, hatch="/")

        # Configurações adicionais do gráfico
        ax.set_xticks(indices_grandes + total_largura / 2)
        ax.set_xticklabels(grupos_grandes, fontsize=14)

        ax.set_ylabel("Time (ms)", fontsize=14)

        plt.grid(True)
        ax.legend()
        plt.tight_layout(rect=[0, 0, 1, 0.85])
        plt.grid(True)

        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
                  borderaxespad=0, ncol=3, fontsize=14)

        # Salva e mostra o gráfico
        plt.savefig(f'{titulo}.png')
        plt.show()


def criar_grafico_de_barras_api(valoresk0s, valoresk3s, valoresk8s, titulo: str):
    operacoes = ['Create Latency', 'Delete Latency', 'Get Latency', 'List Latency', 'Update Latency']
    labels = ['k0s', 'k3s', 'k8s']
    cores = ['grey', 'blue', 'orange', 'black']

    posicoes = list(range(len(operacoes)))
    largura = 0.2

    k0s = [valoresk0s['Create Latency']['Mediana'][1], valoresk0s['Delete Latency']['Mediana'][1],
           valoresk0s['Get Latency']['Mediana'][1], valoresk0s['List Latency']['Mediana'][1],
           valoresk0s['Update Latency']['Mediana'][1]]
    k3s = [valoresk3s['Create Latency']['Mediana'][1], valoresk3s['Delete Latency']['Mediana'][1],
           valoresk3s['Get Latency']['Mediana'][1], valoresk3s['List Latency']['Mediana'][1],
           valoresk3s['Update Latency']['Mediana'][1]]
    k8s = [valoresk8s['Create Latency']['Mediana'][1], valoresk8s['Delete Latency']['Mediana'][1],
           valoresk8s['Get Latency']['Mediana'][1], valoresk8s['List Latency']['Mediana'][1],
           valoresk8s['Update Latency']['Mediana'][1]]

    ic_k0s = [valoresk0s['Create Latency']['Mínimo'][1], valoresk0s['Delete Latency']['Mínimo'][1],
              valoresk0s['Get Latency']['Mínimo'][1], valoresk0s['List Latency']['Mínimo'][1],
              valoresk0s['Update Latency']['Mínimo'][1]]
    ic_k8s = [valoresk8s['Create Latency']['Mínimo'][1], valoresk8s['Delete Latency']['Mínimo'][1],
              valoresk8s['Get Latency']['Mínimo'][1], valoresk8s['List Latency']['Mínimo'][1],
              valoresk8s['Update Latency']['Mínimo'][1]]
    ic_k3s = [valoresk3s['Create Latency']['Mínimo'][1], valoresk3s['Delete Latency']['Mínimo'][1],
              valoresk3s['Get Latency']['Mínimo'][1], valoresk3s['List Latency']['Mínimo'][1],
              valoresk3s['Update Latency']['Mínimo'][1]]

    plt.figure(figsize=(10, 5))
    plt.grid(True)

    plt.bar([p - largura for p in posicoes], k0s, width=largura, label='k0s', color='green', yerr=ic_k0s, capsize=5)
    plt.bar(posicoes, k3s, width=largura, label='k3s', color='blue', yerr=ic_k3s, capsize=5)
    plt.bar([p + largura for p in posicoes], k8s, width=largura, label='k8s', color='orange', yerr=ic_k8s, capsize=5)

    plt.xticks(posicoes, operacoes)

    plt.ylabel("Latency (ms)")

    # Adiciona título e legenda
    # plt.title(titulo)
    plt.legend(['k0s', 'k3s', 'k8s'], bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
               borderaxespad=0, ncol=3)
    # Salva e mostra o gráfico
    # plt.tight_layout(rect=[0, 0, 1, 0.85])
    titulo = titulo.replace(' ', '_').replace('>', '')
    file = f"{titulo}.png"
    plt.savefig(file)
    plt.show()


if __name__ == '__main__':
    for j in range(len(ficheiros)):

        for i in range(1, 31):
            print(f'k3s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs')
            k3sLeitura = open(f'k3s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs', 'r')

            log_content_k3s = k3sLeitura.read()
            extract_results(log_content_k3s)

        estatisticas_deployment_k3s = calcular_estatisticas_das_listas(deployments)
        estatisticas_pod_k3s = calcular_estatisticas_das_listas(pods)
        estatisticas_deployment_api_k3s = calcular_estatisticas_das_listas(deployment_api)
        estatisticas_service_api_k3s = calcular_estatisticas_das_listas(service_api)
        # estatisticas_pod_api_k3s = calcular_estatisticas_das_listas(pod_api)
        # estatisticas_namespace_api_k3s = calcular_estatisticas_das_listas(namespace_api)

        print("Estatísticas dos Pods:")
        print(estatisticas_pod_k3s)
        print("Estatísticas dos Deployments:")
        print(estatisticas_deployment_k3s)

        # print("\nEstatísticas dos Pod API:")
        # print(estatisticas_pod_api_k3s)
        # print("\nEstatísticas dos NameSpace API:")
        # print(estatisticas_namespace_api_k3s)
        print("\nEstatísticas dos Deployment API:")
        print(estatisticas_deployment_api_k3s)
        print("\nEstatísticas dos Service API:")
        print(estatisticas_service_api_k3s)

        k3sGlobal[j]['pods'] = estatisticas_pod_k3s.copy()
        k3sGlobal[j]['deployments'] = estatisticas_deployment_k3s.copy()
        k3sGlobal[j]['deployment_api'] = estatisticas_deployment_api_k3s.copy()
        k3sGlobal[j]['service_api'] = estatisticas_service_api_k3s.copy()
        k3sGlobal[j]['namespace_api'] = namespace_api.copy()
        k3sGlobal[j]['pod_api'] = pod_api.copy()

        pods = {
            'Pod Creation Throughput': [],
            'Pod Client-Server E2E Latency': [],
            'Pod Scheduling Latency Stats': [],
            'Pod Initialization Latency (Kubelet)': [],
            'Pod Starting Latency Stats': [],
            'Pod Creation Avg Latency': [],
            'Pod Startup Total Latency': [],
        }
        pod_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }
        service_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }

        deployment_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }

        namespace_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }

        deployments = {
            'Pod Creation Throughput': [],
            'Pod Client-Server E2E Latency': [],
            'Pod Scheduling Latency Stats': [],
            'Pod Initialization Latency (Kubelet)': [],
            'Pod Starting Latency Stats': [],
            'Pod Creation Avg Latency': [],
            'Pod Startup Total Latency': [],
        }

        for i in range(1, 31):
            print(f'k8s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs')
            k8sLeitura = open(f'k8s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs', 'r')

            log_content_k8s = k8sLeitura.read()
            extract_results(log_content_k8s)

        print(service_api)
        estatisticas_deployment_k8s = calcular_estatisticas_das_listas(deployments)
        estatisticas_pod_k8s = calcular_estatisticas_das_listas(pods)
        # estatisticas_pod_api_k8s = calcular_estatisticas_das_listas(pod_api)
        estatisticas_deployment_api_k8s = calcular_estatisticas_das_listas(deployment_api)
        # estatisticas_namespace_api_k8s = calcular_estatisticas_das_listas(namespace_api)
        estatisticas_service_api_k8s = calcular_estatisticas_das_listas(service_api)

        print("Estatísticas dos Pods:")
        print(estatisticas_pod_k8s)
        print("Estatísticas dos Deployments:")
        print(estatisticas_deployment_k8s)

        # print("\nEstatísticas dos Pod API:")
        # print(estatisticas_pod_api_k8s)
        print("\nEstatísticas dos Deployment API:")
        print(estatisticas_deployment_api_k8s)
        # print("\nEstatísticas dos NameSpace API:")
        # print(estatisticas_namespace_api_k8s)
        print("\nEstatísticas dos Service API:")
        print(estatisticas_service_api_k8s)

        k8sGlobal[j]['pods'] = estatisticas_pod_k8s.copy()

        k8sGlobal[j]['deployments'] = estatisticas_deployment_k8s.copy()
        k8sGlobal[j]['deployment_api'] = estatisticas_deployment_api_k8s.copy()
        k8sGlobal[j]['service_api'] = estatisticas_service_api_k8s.copy()
        k8sGlobal[j]['namespace_api'] = namespace_api.copy()
        k8sGlobal[j]['pod_api'] = pod_api.copy()

        for i in range(1, 31):
            print(f'k0s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs')
            k0sLeitura = open(f'k0s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs', 'r')

            log_content_k0s = k0sLeitura.read()
            extract_results(log_content_k0s)

        estatisticas_deployment_k0s = calcular_estatisticas_das_listas(deployments)
        estatisticas_pod_k0s = calcular_estatisticas_das_listas(pods)
        # estatisticas_pod_api_k0s = calcular_estatisticas_das_listas(pod_api)
        estatisticas_deployment_api_k0s = calcular_estatisticas_das_listas(deployment_api)
        # estatisticas_namespace_api_k0s = calcular_estatisticas_das_listas(namespace_api)
        estatisticas_service_api_k0s = calcular_estatisticas_das_listas(service_api)

        print("Estatísticas dos Pods:")
        print(estatisticas_pod_k0s)
        print("Estatísticas dos Deployments:")
        print(estatisticas_deployment_k0s)

        # print("\nEstatísticas dos Pod API:")
        # print(estatisticas_pod_api_k0s)
        print("\nEstatísticas dos Deployment API:")
        print(estatisticas_deployment_api_k0s)
        # print("\nEstatísticas dos NameSpace API:")
        # print(estatisticas_namespace_api_k0s)
        print("\nEstatísticas dos Service API:")
        print(estatisticas_service_api_k0s)

        k0sGlobal[j]['pods'] = estatisticas_pod_k0s.copy()
        print("!-0", k0sGlobal[j]['pods'])

        k0sGlobal[j]['deployments'] = estatisticas_deployment_k0s.copy()
        k0sGlobal[j]['deployment_api'] = estatisticas_deployment_api_k0s.copy()
        k0sGlobal[j]['service_api'] = estatisticas_service_api_k0s.copy()
        k0sGlobal[j]['namespace_api'] = namespace_api.copy()
        k0sGlobal[j]['pod_api'] = pod_api.copy()

        pods = {
            'Pod Creation Throughput': [],
            'Pod Client-Server E2E Latency': [],
            'Pod Scheduling Latency Stats': [],
            'Pod Initialization Latency (Kubelet)': [],
            'Pod Starting Latency Stats': [],
            'Pod Creation Avg Latency': [],
            'Pod Startup Total Latency': [],
        }
        pod_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }
        service_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }

        deployment_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }

        namespace_api = {

            "Delete Latency": [],
            "Create Latency": [],
            "List Latency": [],
            "Get Latency": [],
            "Update Latency": []
        }
        deployments = {
            'Pod Creation Throughput': [],
            'Pod Client-Server E2E Latency': [],
            'Pod Scheduling Latency Stats': [],
            'Pod Initialization Latency (Kubelet)': [],
            'Pod Starting Latency Stats': [],
            'Pod Creation Avg Latency': [],
            'Pod Startup Total Latency': [],
        }

    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Creation Throughput")
    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Client-Server E2E Latency")
    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Scheduling Latency Stats")
    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Initialization Latency (Kubelet)")
    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Starting Latency Stats")
    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Creation Avg Latency")
    criar_grafico_de_barras_separados(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Startup Total Latency")
    '''
    for i in estatisticas_deployment_k0s.keys():
        criar_grafico_de_barras(estatisticas_deployment_k3s[i], estatisticas_deployment_k8s[i],
                                estatisticas_deployment_k0s[i], "Deployment Statitics --> " + i, ficheiros[j])


                                '''

    # criar_grafico_de_barras_api(data, "Service API --> ")
    # criar_grafico_de_barras_api(estatisticas_pod_api_k0s,estatisticas_pod_api_k3s, estatisticas_pod_api_k8s,f"{ficheiro}-PodAPI")
    # criar_grafico_de_barras_api(estatisticas_namespace_api_k3s[i], estatisticas_namespace_api_k8s[i],estatisticas_namespace_api_k0s[i], f"{ficheiro}-NamespaceAPI")
