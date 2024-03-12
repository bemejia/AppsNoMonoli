import pulsar

service_url = 'pulsar+ssl://pulsar-aws-useast1.streaming.datastax.com:6651'

token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDk1ODgxOTYsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50OzRhZDgzOWUwLTFjNDEtNGE0YS1hZDlmLWZiMjBlMTQ2NTdkNTtibTl0YjI1dmJHbDBhV05oY3c9PTtmYzBiNjQ2Y2RmIiwidG9rZW5pZCI6ImZjMGI2NDZjZGYifQ.hjZL55Fi9lK6gmrkdcmgchx8gC-knnwzcH4c6iDBott8FX8vSSRJLBUq2yhEWDXi_XKp2UPPzlOqzJuBWhjiacLNtNMPrq-1VahJZAof96b4CvJthhRsSBZZN-eMtitW8OWOtx5mkoVNGZOBfSsfpoojZ6soITuSG_tP58VKOQbtarj1du-TlzANYroCQ3wlMRBR7QCphhot7fPtCWDYVkSJu5vpY-9Qh3fyxFFDqmn1WvM0x0hj-ESMoPYIwrN0Nmz3FiXzoMR6tif_95cGvk_2CsVzVWnZO2cYKKruu_j3qf3KdlqxIhdMxw_M_pPv61FgbEsCajeq5NTKpTpUww"
client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))


producer = client.create_producer('persistent://nomonoliticas/default/legal')

for i in range(10):
    print('Sending message %d' % i)
    producer.send(('Hello World! %d' % i).encode('utf-8'))

client.close()