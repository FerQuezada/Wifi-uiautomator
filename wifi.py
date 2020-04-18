#!/usr/bin/python
# C:\Users\fer_q\AppData\Local\Android\Sdk
"""

"""
from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz

#---------------------------------------------------------

def readserial():

    output = check_output(['adb', 'devices'])

    lines = output.splitlines()
    firstDev = lines[1].split()[0]
    print ("1st Device on List = {}".format(firstDev))

    return firstDev



def demo(device,serial):
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
    time.sleep(2)

    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(2)


    # Menu_click
    d(text='Ajustes', className='android.widget.TextView').click()
    time.sleep(2)
    # d.press.back()
    #time.sleep(1)
    #d.press.home()

    return


def wifi(device, serial, wifi_status):
    # Menu_click
    # d(text='ENC', className='android.widget.Switch').click()
    if wifi_status == 'ON':
        if d( text='Apagado', className='android.widget.Switch').exists:
            time.sleep(1)
            print("Status: Wi-Fi Apagado")
            d(text='Apagado', className='android.widget.Switch').click()
            time.sleep(5)
            if d(text='ENC', className='android.widget.Switch').exists:
                print("Wi-Fi Encendido --- Turned On")
        else:
            print("Wi-Fi estaba encendido - No need Turn on")

    if wifi_status == 'OFF':
        if d( text='ENC', className='android.widget.Switch').exists:
            time.sleep(1)
            print("Status: Wi-Fi Encendido")
            d(text='ENC', className='android.widget.Switch').click()
            time.sleep(5)
            if d(text='Apagado', className='android.widget.Switch').exists:
                print("Wi-Fi Apagado --- Turned Off")
        else:
            print("Wi-Fi estaba Apagado - No need Turn Off")

    check_call(
        ['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)

    return

    '''
    try:
        d(text='Apagado', className='android.widget.Switch').click()
        time.sleep(5)
        d.press.back()
        #time.sleep(1)
        #d.press.home()

        return
    except:
        d(text='ENC', className='android.widget.Switch').click()
        time.sleep(5)
        d.press.back()
        return
    '''


#---------------------------------------------------------------------------

if __name__ == "__main__":
    # No arguments are call
    # args = get_arguments()

    firstserial = readserial()
    number_of_repeats = 1

    start_ts = datetime.datetime.now()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    print('test start:  %s '%start_ts_pst)
    # print('serial: %s' % firstserial)
    # print('number of repeats: %s' %number_of_repeats)

    repeats = number_of_repeats  # args.number_of_repeats
    serial = firstserial  # args.serial

    try:
        d = Device(serial)

        print("Script Open Ajustes---------")
        demo(d, serial)
        print("Script Change wifi status---------")
        wifi(d, serial, "ON")
        # time.sleep(5)


    except Exception as ex:
        print(ex)
    finally:

        #stf_dev.release_device()
        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("-------------RESULTS  -------------------------------------------")
        print('test start:  %s' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)