import asyncio
import sys
sys.path.insert(0, 'pywpc/')
sys.path.insert(0, '../../../pywpc/')
import pywpc

async def main():
    print("Start example code...")

    ## Get Python driver version
    print(f'{pywpc.PKG_FULL_NAME} - Version {pywpc.__version__}')

    ## Create device handle
    dev = pywpc.USBDAQF1D()

    ## Connect to network device
    try:
        dev.connect('21JA1044')
    except Exception as err:
        pywpc.printGenericError(err)

    try: 
        ## Get firmware model & version
        driver_info = await dev.sys_getDriverInfo()
        print("Model name: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
 
        ## Open pin0 and pin7 in port 0 with digital output
        port = 0
        pinindex =[0,7]

        await dev.DO_openPins(port, pinindex)

        for i in range(10):
            if i%2 == 0:
                value = [0,1]
            else:
                value = [1,0]

            await dev.DO_writeValuePins(port, pinindex, value) 
            
            print(f'Port: {port}, pinindex = {pinindex}, digital state = {value}') 
            
            await asyncio.sleep(0.5)  ## delay(second)

        ## Wait for 3 seconds
        await asyncio.sleep(3)  ## delay(second)
        
    except Exception as err:
        pywpc.printGenericError(err)

    ## Close pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output 
    await dev.DO_closePins(port, pinindex)
 
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()

    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())
