def recaptchaNOimg(listNum):
    sorted(listNum)
    kk = ''
    for o in sorted(listNum):
        kk += o.partition(':')[2]
    return str(kk)