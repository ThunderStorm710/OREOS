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

ficheiro = "cp_light_4client"

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
    for i in range(1, 31):
        print(f'k3s/{ficheiro}/{ficheiro}_{i}.logs')
        k3s = open(f'k3s/{ficheiro}/{ficheiro}_{i}.logs', 'r')

        log_content_k3s = k3s.read()
        extract_results(log_content_k3s)

    estatisticas_deployment_k3s = calcular_estatisticas_das_listas(deployments)
    estatisticas_pod_k3s = calcular_estatisticas_das_listas(pods)
    # estatisticas_pod_api_k3s = calcular_estatisticas_das_listas(pod_api)
    estatisticas_deployment_api_k3s = calcular_estatisticas_das_listas(deployment_api)
    # estatisticas_namespace_api_k3s = calcular_estatisticas_das_listas(namespace_api)
    estatisticas_service_api_k3s = calcular_estatisticas_das_listas(service_api)

    print("Estatísticas dos Pods:")
    print(estatisticas_pod_k3s)
    print("Estatísticas dos Deployments:")
    print(estatisticas_deployment_k3s)

    # print("\nEstatísticas dos Pod API:")
    # print(estatisticas_pod_api_k3s)
    print("\nEstatísticas dos Deployment API:")
    print(estatisticas_deployment_api_k3s)
    print("\nEstatísticas dos NameSpace API:")
    # print(estatisticas_namespace_api_k3s)
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
        print(f'k8s/{ficheiro}/{ficheiro}_{i}.logs')
        k8s = open(f'k8s/{ficheiro}/{ficheiro}_{i}.logs', 'r')

        log_content_k8s = k8s.read()
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
    print(estatisticas_deployment_api_k8s)
    # print("\nEstatísticas dos NameSpace API:")
    # print(estatisticas_namespace_api_k8s)
    print("\nEstatísticas dos Service API:")
    print(estatisticas_service_api_k8s)

    for i in range(1, 31):
        print(f'k0s/{ficheiro}/{ficheiro}_{i}.logs')
        k0s = open(f'k0s/{ficheiro}/{ficheiro}_{i}.logs', 'r')

        log_content_k0s = k0s.read()
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

    for i in estatisticas_pod_k0s.keys():
        criar_grafico_de_barras(estatisticas_pod_k3s[i], estatisticas_pod_k8s[i],
                                estatisticas_pod_k0s[i], "Pod Statitics --> " + i)

    for i in estatisticas_deployment_k0s.keys():
        criar_grafico_de_barras(estatisticas_deployment_k3s[i], estatisticas_deployment_k8s[i],
                                estatisticas_deployment_k0s[i], "Deployment Statitics --> " + i)

    criar_grafico_de_barras_api(estatisticas_service_api_k0s, estatisticas_service_api_k3s,
                                estatisticas_service_api_k8s, f"{ficheiro}-ServiceAPI")
    criar_grafico_de_barras_api(estatisticas_deployment_api_k0s, estatisticas_deployment_api_k3s,
                                estatisticas_deployment_api_k8s, f"{ficheiro}-DeploymentAPI")
    # criar_grafico_de_barras_api(data, "Service API --> ")
    # criar_grafico_de_barras_api(estatisticas_pod_api_k0s,estatisticas_pod_api_k3s, estatisticas_pod_api_k8s,f"{ficheiro}-PodAPI")
    # criar_grafico_de_barras_api(estatisticas_namespace_api_k3s[i], estatisticas_namespace_api_k8s[i],estatisticas_namespace_api_k0s[i], f"{ficheiro}-NamespaceAPI")
