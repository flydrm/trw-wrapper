from trw_wrapper import TRWClient

API_KEY = ""

def test_all_endpoints():
    print("Probando endpoints gratuitos...")
    free_client = TRWClient()
    
    print("\nVerificando estado de la API:")
    status = free_client.get_status()
    print(f"Status: {status}")

    print("\nProbando bypass gratuito:")
    free_result = free_client.free_bypass(url="https://linkvertise.com/106636/XRayUpdate")
    print(f"Resultado: {free_result}")

    if API_KEY:
        print("\nProbando endpoints autenticados...")
        auth_client = TRWClient(api_key=API_KEY)

        print("\nProbando bypass normal:")
        bypass_result = auth_client.bypass(url="https://linkvertise.com/106636/XRayUpdate")
        print(f"Resultado: {bypass_result}")

        print("\nProbando bypass v2:")
        thread = auth_client.bypass_v2(url="https://linkvertise.com/106636/XRayUpdate")
        print(f"Thread iniciado: {thread}")

        if "ThreadID" in thread:
            print("\nVerificando estado del thread:")
            thread_status = auth_client.check_thread(thread["ThreadID"])
            print(f"Estado: {thread_status}")
    else:
        print("\nNo se encontró API key para probar endpoints autenticados")

if __name__ == "__main__":
    test_all_endpoints() 