from speedtest import Speedtest
st = Speedtest()
print(f"Downloading speed = {st.download()/1000000} MBPS")
print(f"Uploading speed = {st.upload()/1000000} MBPS")
