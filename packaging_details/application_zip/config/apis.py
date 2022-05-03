def get_sensor_data(idx):
    sensorinst=idx->sensor_instance(from db appinst->appid->sensoridx->sensorinstance)
    topicname=sensorinst->regid (db)
    Consumer(topicname)

def get

def controller(idx):
    producer->kafka->

def model_call(idx, **kwargs):
    idx
    idx->modelid
    call mongo->fetch details of model using modulefinder -> ip,port, /predict(common req)
    request.post(ip,port,common req)