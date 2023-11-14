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

pod_creation_throughput = []
pod_client_server_e2e_latency = []
pod_scheduling_latency_stats = []
pod_initialization_latency_kubelet = []
pod_starting_latency_stats = []
pod_creation_avg_latency = []
pod_startup_total_latecy = []

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

    "Delete Pod Latency": [],
    "Create Pod Latency": [],
    "List Pod Latency": [],
    "Get Pod Latency": [],
    "Update Pod Latency": []
}
service_api = {

    "Delete Service Latency": [],
    "Create Service Latency": [],
    "List Service Latency": [],
    "Get Service Latency": [],
    "Update Service Latency": []
}

deployment_api = {

    "Delete Deployment Latency": [],
    "Create Deployment Latency": [],
    "List Deployment Latency": [],
    "Get Deployment Latency": [],
    "Update Deployment Latency": []
}

namespace_api = {

    "Delete Namespace Latency": [],
    "Create Namespace Latency": [],
    "List Namespace Latency": [],
    "Get Namespace Latency": [],
    "Update Namespace Latency": []
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
                pod_api['Delete Pod Latency'].append(l)
            elif "create pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Create Pod Latency'].append(l)
            elif "list pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['List Pod Latency'].append(l)
            elif "get pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Get Pod Latency'].append(l)
            elif "update pod latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Update Pod Latency'].append(l)

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
                deployment_api['Delete Deployment Latency'].append(l)
            elif "create deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Create Deployment Latency'].append(l)
            elif "list deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['List Deployment Latency'].append(l)
            elif "get deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Get Deployment Latency'].append(l)
            elif "update deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Update Deployment Latency'].append(l)

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
                namespace_api['Delete Namespace Latency'].append(l)
            elif "create namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Create Namespace Latency'].append(l)
            elif "list namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['List Namespace Latency'].append(l)
            elif "get namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Get Namespace Latency'].append(l)
            elif "update namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Update Namespace Latency'].append(l)

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
                service_api['Delete Service Latency'].append(l)
            elif "create service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Create Service Latency'].append(l)
            elif "list service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['List Service Latency'].append(l)
            elif "get service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Get Service Latency'].append(l)
            elif "update service latency" in i:
                linha = re.split(":|\t|\"", i)
                # print(linha)
                numeros = linha[6].split()
                # print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Update Service Latency'].append(l)


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
            medias = [np.mean(sublista) for sublista in lista_transposta]
            minI = [-1 for _ in range(4)]
            maxI = [-1 for _ in range(4)]
            for i in range(len(lista_transposta)):
                minI[i], maxI[i] = calcular_intervalo_confianca(lista_transposta[i], 0.05)

            estatisticas[nome] = {
                'Mediana': [minI[0], medias[0], maxI[0]],
                'Mínimo': [minI[1], medias[1], maxI[1]],
                'Máximo': [minI[2], medias[2], maxI[2]],
                # 'Percentil99': medias[3]
            }


        else:
            minI, maxI = calcular_intervalo_confianca(lista, 0.05)

            # Listas simples - calcular estatísticas diretas
            medianas = np.mean(lista)
            minimos = np.mean(lista)
            maximos = np.mean(lista)
            percentil99 = np.mean(lista)

            estatisticas[nome] = {
                'Mediana': [minI, medianas, maxI],
                'Mínimo': [minI, minimos, maxI],
                'Máximo': [minI, maximos, maxI],
                # 'Percentil99': medias[3]
            }

    return estatisticas


def create_boxplot(data, api: bool = True):
    metric_names = list(data.keys())
    if api:
        for metric in metric_names:
            values = data[metric]
            medians = [v[0] for v in values.values()]
            minimums = [v[1] for v in values.values()]
            maximums = [v[2] for v in values.values()]
            percentiles_99 = [v[3] for v in values.values()]

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.boxplot([medians, minimums, maximums, percentiles_99], vert=False)
            ax.set_yticklabels(['Median', 'Minimum', 'Maximum', '99th Percentile'])
            ax.set_xlabel('Values')
            ax.set_title(f'Boxplots for {metric}')

        plt.show()
    else:
        # Criar boxplot para cada conjunto de dados
        for key, value in data.items():
            if isinstance(value['Média'], list):
                means = [value['Média'], value['Mediana'], value['Mínimo'], value['Máximo']]
                create_boxplot1(means, key)
            else:
                create_boxplot1([[value['Média']], [value['Mediana']], [value['Mínimo']], [value['Máximo']]], key)


def create_boxplot1(data, title):
    fig, ax = plt.subplots()
    ax.boxplot(data, vert=False, labels=['Média', 'Mediana', 'Mínimo', 'Máximo'])

    ax.set_title(title)

    plt.show()


def calcular_media(value):
    if isinstance(value['Média'], list):
        return [sum(x) / len(x) for x in zip(*value['Média'])]
    else:
        return value['Média']


def criar_grafico_de_barras(valoresk3s, valoresk8s, valoresk0s, titulo: str):
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
    plt.title(titulo)

    # Define os rótulos do eixo x
    plt.xticks(posicoes, plataformas)
    # plt.xlabel("Mínimo, Mediana e Máximo de cada distribuição")
    plt.ylabel("Time (ms)")

    # Exibe o gráfico de barras
    plt.legend(['k0s','k3s', 'k8s'], loc='upper right', bbox_to_anchor=(1.15, 1.0))
    plt.show()


if __name__ == '__main__':
    for i in range(1, 31):
        print(f'k3s/cp_light_1client/cp_light_1client_{i}.logs')
        k3s = open(f'k3s/cp_light_1client/cp_light_1client_{i}.logs', 'r')

        log_content_k3s = k3s.read()
        extract_results(log_content_k3s)

    estatisticas_deployment_k3s = calcular_estatisticas_das_listas(deployments)
    estatisticas_pod_k3s = calcular_estatisticas_das_listas(pods)
    estatisticas_pod_api_k3s = calcular_estatisticas_das_listas(pod_api)
    estatisticas_deployment_api_k3s = calcular_estatisticas_das_listas(deployment_api)
    estatisticas_namespace_api_k3s = calcular_estatisticas_das_listas(namespace_api)
    estatisticas_service_api_k3s = calcular_estatisticas_das_listas(service_api)

    print("Estatísticas dos Pods:")
    print(estatisticas_pod_k3s)
    print("Estatísticas dos Deployments:")
    print(estatisticas_deployment_k3s)

    print("\nEstatísticas dos Pod API:")
    print(estatisticas_pod_api_k3s)
    print("\nEstatísticas dos Deployment API:")
    print(estatisticas_deployment_api_k3s)
    print("\nEstatísticas dos NameSpace API:")
    print(estatisticas_namespace_api_k3s)
    print("\nEstatísticas dos Service API:")
    print(estatisticas_service_api_k3s)

    pod_creation_throughput = []
    pod_client_server_e2e_latency = []
    pod_scheduling_latency_stats = []
    pod_initialization_latency_kubelet = []
    pod_starting_latency_stats = []
    pod_creation_avg_latency = []
    pod_startup_total_latecy = []

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

        "Delete Pod Latency": [],
        "Create Pod Latency": [],
        "List Pod Latency": [],
        "Get Pod Latency": [],
        "Update Pod Latency": []
    }
    service_api = {

        "Delete Service Latency": [],
        "Create Service Latency": [],
        "List Service Latency": [],
        "Get Service Latency": [],
        "Update Service Latency": []
    }

    deployment_api = {

        "Delete Deployment Latency": [],
        "Create Deployment Latency": [],
        "List Deployment Latency": [],
        "Get Deployment Latency": [],
        "Update Deployment Latency": []
    }

    namespace_api = {

        "Delete Namespace Latency": [],
        "Create Namespace Latency": [],
        "List Namespace Latency": [],
        "Get Namespace Latency": [],
        "Update Namespace Latency": []
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
        print(f'k8s/cp_light_1client/cp_light_1client_{i}.logs')
        k8s = open(f'k8s/cp_light_1client/cp_light_1client_{i}.logs', 'r')

        log_content_k8s = k8s.read()
        extract_results(log_content_k8s)

    print(service_api)
    estatisticas_deployment_k8s = calcular_estatisticas_das_listas(deployments)
    estatisticas_pod_k8s = calcular_estatisticas_das_listas(pods)
    estatisticas_pod_api_k8s = calcular_estatisticas_das_listas(pod_api)
    estatisticas_deployment_api_k8s = calcular_estatisticas_das_listas(deployment_api)
    estatisticas_namespace_api_k8s = calcular_estatisticas_das_listas(namespace_api)
    estatisticas_service_api_k8s = calcular_estatisticas_das_listas(service_api)

    print("Estatísticas dos Pods:")
    print(estatisticas_pod_k8s)
    print("Estatísticas dos Deployments:")
    print(estatisticas_deployment_k8s)

    print("\nEstatísticas dos Pod API:")
    print(estatisticas_pod_api_k8s)
    print("\nEstatísticas dos Deployment API:")
    print(estatisticas_deployment_api_k8s)
    print("\nEstatísticas dos NameSpace API:")
    print(estatisticas_namespace_api_k8s)
    print("\nEstatísticas dos Service API:")
    print(estatisticas_service_api_k8s)

    for i in range(1, 31):
        print(f'k0s/cp_light_1client/cp_light_1client_{i}.logs')
        k0s = open(f'k0s/cp_light_1client/cp_light_1client_{i}.logs', 'r')

        log_content_k0s = k0s.read()
        extract_results(log_content_k0s)

    estatisticas_deployment_k0s = calcular_estatisticas_das_listas(deployments)
    estatisticas_pod_k0s = calcular_estatisticas_das_listas(pods)
    estatisticas_pod_api_k0s = calcular_estatisticas_das_listas(pod_api)
    estatisticas_deployment_api_k0s = calcular_estatisticas_das_listas(deployment_api)
    estatisticas_namespace_api_k0s = calcular_estatisticas_das_listas(namespace_api)
    estatisticas_service_api_k0s = calcular_estatisticas_das_listas(service_api)

    print("Estatísticas dos Pods:")
    print(estatisticas_pod_k0s)
    print("Estatísticas dos Deployments:")
    print(estatisticas_deployment_k0s)

    print("\nEstatísticas dos Pod API:")
    print(estatisticas_pod_api_k0s)
    print("\nEstatísticas dos Deployment API:")
    print(estatisticas_deployment_api_k0s)
    print("\nEstatísticas dos NameSpace API:")
    print(estatisticas_namespace_api_k0s)
    print("\nEstatísticas dos Service API:")
    print(estatisticas_service_api_k0s)

    pod_creation_throughput = []
    pod_client_server_e2e_latency = []
    pod_scheduling_latency_stats = []
    pod_initialization_latency_kubelet = []
    pod_starting_latency_stats = []
    pod_creation_avg_latency = []
    pod_startup_total_latecy = []

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

        "Delete Pod Latency": [],
        "Create Pod Latency": [],
        "List Pod Latency": [],
        "Get Pod Latency": [],
        "Update Pod Latency": []
    }
    service_api = {

        "Delete Service Latency": [],
        "Create Service Latency": [],
        "List Service Latency": [],
        "Get Service Latency": [],
        "Update Service Latency": []
    }

    deployment_api = {

        "Delete Deployment Latency": [],
        "Create Deployment Latency": [],
        "List Deployment Latency": [],
        "Get Deployment Latency": [],
        "Update Deployment Latency": []
    }

    namespace_api = {

        "Delete Namespace Latency": [],
        "Create Namespace Latency": [],
        "List Namespace Latency": [],
        "Get Namespace Latency": [],
        "Update Namespace Latency": []
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



    for i in estatisticas_pod_k0s.keys():
        criar_grafico_de_barras(estatisticas_pod_k3s[i], estatisticas_pod_k8s[i],
                                estatisticas_pod_k0s[i], "Pod Statitics --> " + i)

    for i in estatisticas_deployment_k0s.keys():
        criar_grafico_de_barras(estatisticas_deployment_k3s[i], estatisticas_deployment_k8s[i],
                                estatisticas_deployment_k0s[i], "Deployment Statitics --> " + i)

    for i in estatisticas_service_api_k0s.keys():
        criar_grafico_de_barras(estatisticas_service_api_k3s[i], estatisticas_service_api_k8s[i],
                                estatisticas_service_api_k0s[i], "Service API --> " + i)

    for i in estatisticas_pod_api_k0s.keys():
        criar_grafico_de_barras(estatisticas_pod_api_k3s[i], estatisticas_pod_api_k8s[i], estatisticas_pod_api_k0s[i],
                                "Pod API --> " + i)

    for i in estatisticas_deployment_api_k0s.keys():
        criar_grafico_de_barras(estatisticas_deployment_api_k3s[i], estatisticas_deployment_api_k8s[i],
                                estatisticas_deployment_api_k0s[i], "Deployment API -->  " + i)

    for i in estatisticas_namespace_api_k0s.keys():
        criar_grafico_de_barras(estatisticas_namespace_api_k3s[i], estatisticas_namespace_api_k8s[i],
                                estatisticas_namespace_api_k0s[i], "Namespace API --> " + i)
