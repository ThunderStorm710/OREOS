import numpy as np
import re
import matplotlib.pyplot as plt
from scipy import stats

pod_results_pattern = re.compile(r'Pod Results(.+?)Pod Creation Success Rate: ([\d.]+) %', re.DOTALL)
deployment_results_pattern = re.compile(r'Deployment Results(.+?)Pod Creation Success Rate: ([\d.]+) %', re.DOTALL)
namespace_results_pattern = re.compile(r'Namespace Results(.+?)Service API Call Latencies \(ms\)', re.DOTALL)
namespace_results_pattern1 = re.compile(r'Namespace Results(.+?)Benchmark run completed.', re.DOTALL)
service_results_pattern = re.compile(r'Service Results(.+?)Benchmark run completed.', re.DOTALL)

ficheiros = ["cp_light_1client", "cp_light_4client", "cp_heavy_8client", "cp_heavy_12client", "cp_heavy_16client",
             "cp_heavy_20client", "cp_heavy_24client"]

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

heavy_16 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
            'service_api': service_api.copy(),
            'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}

heavy_20 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
            'service_api': service_api.copy(),
            'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}

heavy_24 = {'pods': pods.copy(), 'deployments': deployments.copy(), 'pods_api': pod_api.copy(),
            'service_api': service_api.copy(),
            'namespace_api': namespace_api.copy(), 'deployments_api': deployment_api.copy()}

k0sGlobal = [light_1.copy(), light_4.copy(), heavy_8.copy(), heavy_12.copy(), heavy_16.copy(), heavy_20.copy(),
             heavy_24.copy()]
k3sGlobal = [light_1.copy(), light_4.copy(), heavy_8.copy(), heavy_12.copy(), heavy_16.copy(), heavy_20.copy(),
             heavy_24.copy()]
k8sGlobal = [light_1.copy(), light_4.copy(), heavy_8.copy(), heavy_12.copy(), heavy_16.copy(), heavy_20.copy(),
             heavy_24.copy()]


def extract_results(log_content):
    """
    This function extracts the results from the log file and stores them in the dictionaries
    @:param log_content: log file content
    @:return: split dictionaries with the results of the log file
    """
    pod_results_match = pod_results_pattern.search(log_content)
    deployment_results_match = deployment_results_pattern.search(log_content)
    namespace_results_match = namespace_results_pattern.search(log_content)
    namespace_results_match1 = namespace_results_pattern1.search(log_content)
    service_results_match = service_results_pattern.search(log_content)

    if pod_results_match:
        pod_results_content = pod_results_match.group(1).strip()
        pod_success_rate = pod_results_match.group(2).strip()
        lista = pod_results_content.split("\n")
        for i in lista:
            if "Pod creation throughput (pods/minutes):" in i:
                linha = re.split(":|\t|\"", i)
                pods['Pod Creation Throughput'].append(float(linha[6]))

            elif "Pod creation average latency" in i:
                linha = re.split(":|\t|\"", i)
                pods['Pod Creation Avg Latency'].append(float(linha[6]))

            elif "Pod startup total latency (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Startup Total Latency'].append(l)

            elif "Pod client-server e2e latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Client-Server E2E Latency'].append(l)

            elif "Pod scheduling latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Scheduling Latency Stats'].append(l)

            elif "Pod initialization latency on kubelet (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Initialization Latency (Kubelet)'].append(l)

            elif "Pod starting latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Starting Latency Stats'].append(l)


            elif "delete pod latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Delete Latency'].append(l)
            elif "create pod latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Create Latency'].append(l)
            elif "list pod latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['List Latency'].append(l)
            elif "get pod latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Get Latency'].append(l)
            elif "update pod latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Update Latency'].append(l)

        print(f"Pod Success Rate: {pod_success_rate}%")

    if deployment_results_match:
        deployment_results_content = deployment_results_match.group(1).strip()
        deployment_success_rate = deployment_results_match.group(2).strip()
        print(f"Deployment Success Rate: {deployment_success_rate}%")

        lista = deployment_results_content.split("\n")
        for i in lista:
            if "Pod creation throughput (pods/minutes):" in i:
                linha = re.split(":|\t|\"", i)
                deployments['Pod Creation Throughput'].append(float(linha[6]))

            elif "Pod creation average latency" in i:
                linha = re.split(":|\t|\"", i)
                deployments['Pod Creation Avg Latency'].append(float(linha[6]))

            elif "Pod startup total latency (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Startup Total Latency'].append(l)

            elif "Pod client-server e2e latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Client-Server E2E Latency'].append(l)

            elif "Pod scheduling latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Scheduling Latency Stats'].append(l)

            elif "Pod initialization latency on kubelet (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Initialization Latency (Kubelet)'].append(l)

            elif "Pod starting latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Starting Latency Stats'].append(l)


            elif "delete deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Delete Latency'].append(l)
            elif "create deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Create Latency'].append(l)
            elif "list deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['List Latency'].append(l)
            elif "get deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Get Latency'].append(l)
            elif "update deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Update Latency'].append(l)

    if namespace_results_match or namespace_results_match1:
        if namespace_results_match:
            namespace_results_content = namespace_results_match.group(1).strip()
        else:
            namespace_results_content = namespace_results_match1.group(1).strip()

        lista = namespace_results_content.split("\n")
        for i in lista:
            if "delete namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Delete Latency'].append(l)
            elif "create namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Create Latency'].append(l)
            elif "list namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['List Latency'].append(l)
            elif "get namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Get Latency'].append(l)
            elif "update namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Update Latency'].append(l)

    if service_results_match:
        service_results_content = service_results_match.group(1).strip()
        lista = service_results_content.split("\n")
        for i in lista:
            if "delete service latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Delete Latency'].append(l)
            elif "create service latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Create Latency'].append(l)
            elif "list service latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['List Latency'].append(l)
            elif "get service latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Get Latency'].append(l)
            elif "update service latency" in i:
                linha = re.split(":|\t|\"", i)
                numeros = linha[6].split()
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Update Latency'].append(l)


def confidence_interval(dados, alpha):
    """
    This function calculates the confidence interval of a given data set
    @:param dados: data list
    @:param alpha: confidence level
    """
    dados = outliers_cleaning(dados)
    media = np.mean(dados)
    desvio_padrao = np.std(dados, ddof=1)
    tamanho_amostra = len(dados)
    t_valor = stats.t.ppf(1 - alpha / 2, tamanho_amostra - 1)

    margem_erro = t_valor * (desvio_padrao / np.sqrt(tamanho_amostra))

    intervalo_inferior = media - margem_erro
    intervalo_superior = media + margem_erro

    if intervalo_inferior < 0:
        intervalo_inferior = 1

    return intervalo_inferior, intervalo_superior


def outliers_cleaning(data):
    """
    This function removes the outliers from a given data set
    :param data: list of data
    :return: list of data without outliers
    """
    if type(data) != list:
        data = data.tolist()
    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = 2

    outliers = (data < (mean - threshold * std_dev)) | (data > (mean + threshold * std_dev))
    outliers = outliers.tolist()
    i = 0
    while i < len(data):
        if outliers[i]:
            data.pop(i)
            outliers.pop(i)
            i = 0
        i += 1
    return data


def statistics_calculation(listas):
    """
    This function calculates the statistics of a given data set
    :param listas: dictionary of data lists
    :return: dictionary of statistics
    """
    estatisticas = {}

    for nome, lista in listas.items():

        if isinstance(lista[0], list):
            lista_transposta = np.array(lista).T
            medias = [np.mean(sublista) for sublista in lista_transposta]
            minI = [0 for _ in range(4)]
            maxI = [0 for _ in range(4)]
            for i in range(len(lista_transposta)):
                minI[i], maxI[i] = confidence_interval(lista_transposta[i], 0.05)

            estatisticas[nome] = {
                'Mediana': [minI[0], medias[0], maxI[0]],
                'Mínimo': [minI[1], medias[1], maxI[1]],
                'Máximo': [minI[2], medias[2], maxI[2]],
            }


        else:
            minI, maxI = confidence_interval(lista, 0.05)

            medianas = np.mean(lista)
            minimos = np.mean(lista)
            maximos = np.mean(lista)

            estatisticas[nome] = {
                'Mediana': [minI, medianas, maxI],
                'Mínimo': [minI, minimos, maxI],
                'Máximo': [minI, maximos, maxI],
            }

    return estatisticas


def bar_plots_latency_statistics(valoresk0s, valoresk3s, valoresk8s, titulo, grupos_grandes: list, pods: str = 'pods'):
    subgrupos = ['Mínimo', 'Mediana', 'Máximo']
    nomes = ['Minimum', 'Median', 'Maximum']
    cores = ['blue', 'green', 'orange']

    largura = 0.1

    if titulo == "Pod Creation Throughput" or titulo == "Pod Creation Avg Latency":
        espaco_entre_grupos = 0.2

        total_largura = largura + espaco_entre_grupos
        indices_grandes = np.arange(len(grupos_grandes)) * (total_largura + espaco_entre_grupos)

        fig, ax = plt.subplots(figsize=(12, 6))

        for i, grupo in enumerate(grupos_grandes):
            posicao_grupo = indices_grandes[i]

            valor_k0s = valoresk0s[i][pods][titulo]['Mediana'][1]
            ic_k0s = (valoresk0s[i][pods][titulo]['Mediana'][2] - valoresk0s[i][pods][titulo]['Mediana'][0]) / 2
            ax.bar(posicao_grupo, valor_k0s, largura, yerr=ic_k0s, label='k0s', color=cores[0], capsize=2, hatch="\\")

            valor_k3s = valoresk3s[i][pods][titulo]['Mediana'][1]
            ic_k3s = (valoresk3s[i][pods][titulo]['Mediana'][2] - valoresk3s[i][pods][titulo]['Mediana'][0]) / 2
            ax.bar(posicao_grupo + largura, valor_k3s, largura, yerr=ic_k3s, label='k3s', color=cores[1], capsize=2,
                   hatch=".")

            valor_k8s = valoresk8s[i][pods][titulo]['Mediana'][1]
            ic_k8s = (valoresk8s[i][pods][titulo]['Mediana'][2] - valoresk8s[i][pods][titulo]['Mediana'][0]) / 2
            ax.bar(posicao_grupo + largura * 2, valor_k8s, largura, yerr=ic_k8s, label='k8s', color=cores[2], capsize=2,
                   hatch="+")

        ax.set_xticks(indices_grandes + 0.1)
        ax.set_xticklabels(grupos_grandes, fontsize=24)
        ax.set_ylabel("Throughput (pods/min)", fontsize=24)

        plt.grid(True)
        plt.legend(['k0s', 'k3s', 'k8s'], bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
                   borderaxespad=0, ncol=3, fontsize=16, frameon=False)
        plt.tight_layout(rect=[0, 0, 1, 1])
        plt.grid(True)

        if pods == 'pods':
            plt.savefig(f'{titulo}.png')
        else:
            plt.savefig(f'Deployments - {titulo}.png')

        plt.show()
    else:
        espaco_entre_grupos = 0.4
        largura = 0.1
        num_subgrupos = len(subgrupos)
        total_largura = (num_subgrupos * largura) + ((num_subgrupos - 1) * espaco_entre_grupos)
        indices_grandes = np.arange(len(grupos_grandes)) * (total_largura + 2 * espaco_entre_grupos)

        fig, ax = plt.subplots(figsize=(15, 6))
        hatch = ''

        for i, subgrupo in enumerate(subgrupos):
            posicoes = indices_grandes + (i * (largura + espaco_entre_grupos))

            valores_k0s = [valoresk0s[grupo][pods][titulo][subgrupo][1] for grupo in range(len(grupos_grandes))]

            if subgrupo == 'Mínimo':
                hatch = '\\'
            if subgrupo == 'Mediana':
                hatch = '.'
            if subgrupo == 'Máximo':
                hatch = '+'
            ic_k0s = [(valoresk0s[grupo][pods][titulo][subgrupo][2] - valoresk0s[grupo][pods][titulo][subgrupo][0]) / 2
                      for grupo in
                      range(len(grupos_grandes))]
            ax.bar(posicoes, valores_k0s, largura, yerr=ic_k0s, label=f'k0s - {nomes[i]}', color=cores[0],
                   capsize=2, hatch=hatch)

            valores_k3s = [valoresk3s[grupo][pods][titulo][subgrupo][1] for grupo in range(len(grupos_grandes))]
            ic_k3s = [(valoresk3s[grupo][pods][titulo][subgrupo][2] - valoresk3s[grupo][pods][titulo][subgrupo][0]) / 2
                      for grupo in range(len(grupos_grandes))]
            ax.bar(posicoes + largura, valores_k3s, largura, yerr=ic_k3s, label=f'k3s - {nomes[i]} ',
                   color=cores[1],
                   capsize=2, hatch=hatch)

            valores_k8s = [valoresk8s[grupo][pods][titulo][subgrupo][1] for grupo in range(len(grupos_grandes))]
            ic_k8s = [(valoresk8s[grupo][pods][titulo][subgrupo][2] - valoresk8s[grupo][pods][titulo][subgrupo][0]) / 2
                      for grupo in range(len(grupos_grandes))]
            ax.bar(posicoes + largura * 2, valores_k8s, largura, yerr=ic_k8s, label=f'k8s - {nomes[i]}',
                   color=cores[2],
                   capsize=2, hatch=hatch)

        ax.set_xticks(indices_grandes + total_largura / 2)
        ax.set_xticklabels(grupos_grandes, fontsize=24)

        ax.set_ylabel("Time (ms)", fontsize=24)

        plt.grid(True)
        ax.legend()
        plt.tight_layout(rect=[0, 0, 1, 0.8])
        plt.grid(True)

        ax.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
                  borderaxespad=0, ncol=3, fontsize=20, frameon=False)

        if pods == 'pods':
            plt.savefig(f'{titulo}.png')
        else:
            plt.savefig(f'Deployments - {titulo}.png')
        plt.show()


def bar_plots_api_statistics(valoresk0s, valoresk3s, valoresk8s, titulo: str):
    operacoes = ['Create', 'Delete', 'Get', 'List', 'Update']

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

    ic_k0s = [(valoresk0s['Create Latency']['Mediana'][2] - valoresk0s['Create Latency']['Mediana'][0]) / 2,
              (valoresk0s['Delete Latency']['Mediana'][2] - valoresk0s['Delete Latency']['Mediana'][0]) / 2,
              (valoresk0s['Get Latency']['Mediana'][2] - valoresk0s['Get Latency']['Mediana'][0]) / 2,
              (valoresk0s['List Latency']['Mediana'][2] - valoresk0s['List Latency']['Mediana'][0]) / 2,
              (valoresk0s['Update Latency']['Mediana'][2] - valoresk0s['Update Latency']['Mediana'][0]) / 2]
    ic_k8s = [(valoresk8s['Create Latency']['Mediana'][2] - valoresk8s['Create Latency']['Mediana'][0]) / 2,
              (valoresk8s['Delete Latency']['Mediana'][2] - valoresk8s['Delete Latency']['Mediana'][0]) / 2,
              (valoresk8s['Get Latency']['Mediana'][2] - valoresk8s['Get Latency']['Mediana'][0]) / 2,
              (valoresk8s['List Latency']['Mediana'][2] - valoresk8s['List Latency']['Mediana'][0]) / 2,
              (valoresk8s['Update Latency']['Mediana'][2] - valoresk8s['Update Latency']['Mediana'][0]) / 2]
    ic_k3s = [(valoresk3s['Create Latency']['Mediana'][2] - valoresk3s['Create Latency']['Mediana'][0]) / 2,
              (valoresk3s['Delete Latency']['Mediana'][2] - valoresk3s['Delete Latency']['Mediana'][0]) / 2,
              (valoresk3s['Get Latency']['Mediana'][2] - valoresk3s['Get Latency']['Mediana'][0]) / 2,
              (valoresk3s['List Latency']['Mediana'][2] - valoresk3s['List Latency']['Mediana'][0]) / 2,
              (valoresk3s['Update Latency']['Mediana'][2] - valoresk3s['Update Latency']['Mediana'][0]) / 2]

    plt.figure(figsize=(10, 5))
    plt.grid(True)

    plt.bar([p - largura for p in posicoes], k0s, width=largura, label='k0s', color='blue', yerr=ic_k0s, capsize=5,
            hatch="\\")
    plt.bar(posicoes, k3s, width=largura, label='k3s', color='green', yerr=ic_k3s, capsize=5, hatch=".")
    plt.bar([p + largura for p in posicoes], k8s, width=largura, label='k8s', color='orange', yerr=ic_k8s, capsize=5,
            hatch="+")

    plt.xticks(posicoes, operacoes, fontsize=16)

    plt.ylabel("Latency (ms)", fontsize=16)

    plt.legend(['k0s', 'k3s', 'k8s'], bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand",
               borderaxespad=0, ncol=3, frameon=False, fontsize=16)

    plt.savefig(titulo)
    plt.show()


if __name__ == '__main__':
    for j in range(len(ficheiros)):

        for i in range(1, 31):
            print(f'k3s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs')
            k3sLeitura = open(f'k3s/{ficheiros[j]}/{ficheiros[j]}_{i}.logs', 'r')

            log_content_k3s = k3sLeitura.read()
            extract_results(log_content_k3s)

        estatisticas_deployment_k3s = statistics_calculation(deployments)
        estatisticas_pod_k3s = statistics_calculation(pods)
        estatisticas_deployment_api_k3s = statistics_calculation(deployment_api)
        estatisticas_service_api_k3s = statistics_calculation(service_api)
        estatisticas_pod_api_k3s = statistics_calculation(pod_api)
        estatisticas_namespace_api_k3s = statistics_calculation(namespace_api)

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

        estatisticas_deployment_k8s = statistics_calculation(deployments)
        estatisticas_pod_k8s = statistics_calculation(pods)
        estatisticas_pod_api_k8s = statistics_calculation(pod_api)
        estatisticas_deployment_api_k8s = statistics_calculation(deployment_api)
        estatisticas_namespace_api_k8s = statistics_calculation(namespace_api)
        estatisticas_service_api_k8s = statistics_calculation(service_api)

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

        estatisticas_deployment_k0s = statistics_calculation(deployments)
        estatisticas_pod_k0s = statistics_calculation(pods)
        estatisticas_pod_api_k0s = statistics_calculation(pod_api)
        estatisticas_deployment_api_k0s = statistics_calculation(deployment_api)
        estatisticas_namespace_api_k0s = statistics_calculation(namespace_api)
        estatisticas_service_api_k0s = statistics_calculation(service_api)

        k0sGlobal[j]['pods'] = estatisticas_pod_k0s.copy()
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

    groups = ['1 pod', '4 pods', '8 pods', '12 pods', '16 pods', '20 pods', '24 pods']
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Creation Throughput", groups)
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Client-Server E2E Latency",
                                 groups)
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Scheduling Latency Stats", groups)
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Initialization Latency (Kubelet)",
                                 groups)
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Starting Latency Stats", groups)
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Creation Avg Latency", groups)
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Startup Total Latency", groups)

    groups = ['5 pod', '20 pods', '40 pods', '60 pods', '80 pods', '100 pods', '120 pods']
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Creation Throughput", groups,
                                 'deployments')
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Client-Server E2E Latency",
                                 groups, 'deployments')
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Scheduling Latency Stats", groups,
                                 'deployments')
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Initialization Latency (Kubelet)",
                                 groups, 'deployments')
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Starting Latency Stats", groups,
                                 'deployments')
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Creation Avg Latency", groups,
                                 'deployments')
    bar_plots_latency_statistics(k0sGlobal, k3sGlobal, k8sGlobal, "Pod Startup Total Latency", groups,
                                 'deployments')

    bar_plots_api_statistics(k0sGlobal[0]['service_api'], k3sGlobal[0]['service_api'], k8sGlobal[0]['service_api'],
                             f"1 pod - CRUD - Service API")
    bar_plots_api_statistics(k0sGlobal[1]['service_api'], k3sGlobal[1]['service_api'], k8sGlobal[1]['service_api'],
                             f"4 pod - CRUD - Service API")
    bar_plots_api_statistics(k0sGlobal[2]['service_api'], k3sGlobal[2]['service_api'], k8sGlobal[2]['service_api'],
                             f"8 pod - CRUD - Service API")
    bar_plots_api_statistics(k0sGlobal[3]['service_api'], k3sGlobal[3]['service_api'], k8sGlobal[3]['service_api'],
                             f"12 pod - CRUD - Service API")
    bar_plots_api_statistics(k0sGlobal[4]['service_api'], k3sGlobal[4]['service_api'], k8sGlobal[4]['service_api'],
                             f"16 pod - CRUD - Service API")
    bar_plots_api_statistics(k0sGlobal[5]['service_api'], k3sGlobal[5]['service_api'], k8sGlobal[5]['service_api'],
                             f"20 pod - CRUD - Service API")
    bar_plots_api_statistics(k0sGlobal[6]['service_api'], k3sGlobal[6]['service_api'], k8sGlobal[6]['service_api'],
                             f"24 pod - CRUD - Service API")
