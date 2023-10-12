import numpy as np
import re

# Define regular expressions for extracting relevant information
pod_results_pattern = re.compile(r'Pod Results(.+?)Pod Creation Success Rate: ([\d.]+) %', re.DOTALL)
deployment_results_pattern = re.compile(r'Deployment Results(.+?)Pod Creation Success Rate: ([\d.]+) %', re.DOTALL)
namespace_results_pattern = re.compile(r'Namespace Results(.+?)Service API Call Latencies \(ms\)', re.DOTALL)
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
    service_results_match = service_results_pattern.search(log_content)

    if pod_results_match:
        pod_results_content = pod_results_match.group(1).strip()
        pod_success_rate = pod_results_match.group(2).strip()
        print("Pod Results:")
        print(pod_results_content)
        lista = pod_results_content.split("\n")
        for i in lista:
            if "Pod creation throughput (pods/minutes):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                print(float(linha[6]))
                pods['Pod Creation Throughput'].append(float(linha[6]))

            elif "Pod creation average latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                print(float(linha[6]))
                pods['Pod Creation Avg Latency'].append(float(linha[6]))

            elif "Pod startup total latency (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Startup Total Latency'].append(l)

            elif "Pod client-server e2e latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Client-Server E2E Latency'].append(l)

            elif "Pod scheduling latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Scheduling Latency Stats'].append(l)

            elif "Pod initialization latency on kubelet (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Initialization Latency (Kubelet)'].append(l)

            elif "Pod starting latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pods['Pod Starting Latency Stats'].append(l)


            elif "delete pod latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Delete Pod Latency'].append(l)
            elif "create pod latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Create Pod Latency'].append(l)
            elif "list pod latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['List Pod Latency'].append(l)
            elif "get pod latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Get Pod Latency'].append(l)
            elif "update pod latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                pod_api['Update Pod Latency'].append(l)

        print(f"Pod Success Rate: {pod_success_rate}%")

    if deployment_results_match:
        deployment_results_content = deployment_results_match.group(1).strip()
        deployment_success_rate = deployment_results_match.group(2).strip()
        print("\nDeployment Results:")
        print(deployment_results_content)
        print(f"Deployment Success Rate: {deployment_success_rate}%")

        lista = deployment_results_content.split("\n")
        for i in lista:
            if "Pod creation throughput (pods/minutes):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                print(float(linha[6]))
                deployments['Pod Creation Throughput'].append(float(linha[6]))

            elif "Pod creation average latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                print(float(linha[6]))
                deployments['Pod Creation Avg Latency'].append(float(linha[6]))

            elif "Pod startup total latency (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Startup Total Latency'].append(l)

            elif "Pod client-server e2e latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Client-Server E2E Latency'].append(l)

            elif "Pod scheduling latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Scheduling Latency Stats'].append(l)

            elif "Pod initialization latency on kubelet (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Initialization Latency (Kubelet)'].append(l)

            elif "Pod starting latency stats (client):" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployments['Pod Starting Latency Stats'].append(l)


            elif "delete deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Delete Deployment Latency'].append(l)
            elif "create deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Create Deployment Latency'].append(l)
            elif "list deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['List Deployment Latency'].append(l)
            elif "get deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Get Deployment Latency'].append(l)
            elif "update deployment latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                deployment_api['Update Deployment Latency'].append(l)

    if namespace_results_match:
        namespace_results_content = namespace_results_match.group(1).strip()
        print("\nNamespace Results:")
        print(namespace_results_content)
        lista = namespace_results_content.split("\n")
        for i in lista:
            if "delete namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Delete Namespace Latency'].append(l)
            elif "create namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Create Namespace Latency'].append(l)
            elif "list namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['List Namespace Latency'].append(l)
            elif "get namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Get Namespace Latency'].append(l)
            elif "update namespace latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                namespace_api['Update Namespace Latency'].append(l)

    if service_results_match:
        service_results_content = service_results_match.group(1).strip()
        print("\nService Results:")
        print(service_results_content)
        lista = service_results_content.split("\n")
        for i in lista:
            if "delete service latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Delete Service Latency'].append(l)
            elif "create service latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Create Service Latency'].append(l)
            elif "list service latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['List Service Latency'].append(l)
            elif "get service latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Get Service Latency'].append(l)
            elif "update service latency" in i:
                linha = re.split(":|\t|\"", i)
                print(linha)
                numeros = linha[6].split()
                print(numeros)
                l = []
                for j in numeros:
                    l.append(float(j))
                service_api['Update Service Latency'].append(l)


def calcular_estatisticas_das_listas(listas):
    estatisticas = {}

    for nome, lista in listas.items():
        if isinstance(lista[0], list):
            # Sublistas - calcular estatísticas por índice
            medias = np.mean(lista, axis=0)
            medianas = np.median(lista, axis=0)
            minimos = np.min(lista, axis=0)
            maximos = np.max(lista, axis=0)
        else:
            # Listas simples - calcular estatísticas diretas
            medias = np.mean(lista)
            medianas = np.median(lista)
            minimos = np.min(lista)
            maximos = np.max(lista)

        estatisticas[nome] = {
            'Média': medias.tolist(),
            'Mediana': medianas.tolist(),
            'Mínimo': minimos.tolist(),
            'Máximo': maximos.tolist()
        }

    return estatisticas


if __name__ == '__main__':
    for i in range(1, 31):
        print(f'k8s/cp_heavy_12client/cp_heavy_12client_{i}.logs')
        with open(f'k8s/cp_heavy_12client/cp_heavy_12client_{i}.logs', 'r') as file:
            log_content = file.read()
            extract_results(log_content)
    # Call the function to extract and print the results

    print(deployments)
    print(pod_api)
    print(service_api)
    print(namespace_api)
    print(deployment_api)

    estatisticas_deployment = calcular_estatisticas_das_listas(deployments)
    estatisticas_pod = calcular_estatisticas_das_listas(pods)
    estatisticas_pod_api = calcular_estatisticas_das_listas(pod_api)
    estatisticas_deployment_api = calcular_estatisticas_das_listas(deployment_api)
    estatisticas_namespace_api = calcular_estatisticas_das_listas(namespace_api)
    estatisticas_service_api = calcular_estatisticas_das_listas(service_api)

    print("Estatísticas dos Pods:")
    print(estatisticas_pod)
    print("Estatísticas dos Deployments:")
    print(estatisticas_deployment)

    print("\nEstatísticas dos Pod API:")
    print(estatisticas_pod_api)
    print("\nEstatísticas dos Deployment API:")
    print(estatisticas_deployment_api)
    print("\nEstatísticas dos NameSpace API:")
    print(estatisticas_namespace_api)
    print("\nEstatísticas dos Service API:")
    print(estatisticas_service_api)
