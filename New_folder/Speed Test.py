import speedtest
st =  speedtest.Speedtest()
option = int(input('''What speed you want to test:
1) Download speed
2) Upload speed
3) Ping
Your choice: '''))

if option == 1:
    print(st.download(), 'b/s')
elif option == 2:
    print(st.upload(), 'b/s')
elif option == 3:
    servername = []
    st.get_servers(servername)
    print(st.results.ping, 'b/s')
