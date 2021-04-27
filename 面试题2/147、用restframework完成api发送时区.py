# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/24--21:00
import time
class getCurrenttime(APIView):
    def get(self,request):
        local_time = time.locatime()
        time_zone = settings.TIME_ZONE
        temp = {'localtime':local_time,'timezone':time_zone}
        return Response(temp)