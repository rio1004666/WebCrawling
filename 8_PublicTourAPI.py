

import urllib.request
req = urllib.request
ServiceKey = '9QgVOvWq33%2FyqmZYgpwoLnmqRFRtq%2FyDWIkkgDOVPWcfqRQQgHS6lHTeF4ZH%2BncmgOOlcJD1aW%2FCIzQlos9gFg%3D%3D'
url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
parameters = "?_type=json&serviceKey=" + ServiceKey
parameters += "&YM=201201"
parameters += "&NAT_CO=112"
parameters += "ED_CD=D"

request = req.Request(url + parameters)
request.get_method = lambda: 'GET'
response_body = req.urlopen(request).read()
print(response_body)