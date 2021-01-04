import requests

headers = {
    'Cookie': 'Ecp_ClientId=3200129204301416324; SERVERID=Server1; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMTIwMTkxMTMwMjI5IiwiZ3JvdXBzIjpbNSwxXSwiaWF0IjoxNjA5NzI0MDMwLCJleHAiOjE2MDk4MTA0MzB9.6pCZZpuCC7wf_p947aYzCFGcgofQ4jKdvcfyuVV2NGU; webvpn_username=120191130229%7C1609724030%7C1e3edd387f44ccf00705055b3bd5a35de9976f3c; _astraeus_session=T2d2UmI3N3hDS1NDcDZ4SGtFOEpyS3pqUXM2M1k4Ym8xbTI5NHZ3Y2R0N1BMb3o3ODFJSTg5VFlnWTNZUTZ1NWtubURnejMvTXVybUVGVUtHYVdkd2Nxc1FpejlBRlFjU1hhLzUxU0MwRittaEoyNFZqRng0ZmNFa080OERqV1dUUXVKU1lCVGFXdWtKbFM1TXZub2s1bmVhMWErU3diVTJwUEdJVnBLKy9BblpjM1pTL29GeXRxVGV4ZUlNQUVIRmF6ZUw1UndheVF5dWFCRTg3SGR0eHpNaFh1dTFtcTF1M0ZVc21UMnhDam5TY0w0NGl1SkkrQzB4ZUtBdUQ3aE5jSG8rQUgvVE0zVDI4Zk5CS096UVVKczhIZ2dWZVhjRXhseC9kZDZYei8wUVZLNklxSlZxR3hlclpDMGlaY0RCZ0tHN3JNUUZBQTF0TDlDZTVwUVdRPT0tLTRvczdhQUwxNU1obHk5amR1ak96aUE9PQ%3D%3D--ad753a81497eab308f933ebc1b02144e3f7fd130',
    'Host': 'webvpn.ncepu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
s = requests.Session()
s.get('https://webvpn.ncepu.edu.cn/users/sign_in', headers=headers)
print(type(s))
r = s.get('https://webvpn.ncepu.edu.cn/')

print(r.text)
