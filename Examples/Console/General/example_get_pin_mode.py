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
        print("Firmware model: " + driver_info[0])
        print("Firmware version: " + driver_info[-1])
        
        ## Get pinmode from port 0 to port 3
        for i in range(4):
            pin_mode_status = await dev.sys_getPinModeInPort(i)
            print(f'pins: {pin_mode_status[0]}, slot{i}, mode {pin_mode_status[1]}') 

            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)
        print()
        print("====================")

        port_DO = 0
        port_DI = 1
        ## Open pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output
        await dev.DO_openPins(port_DO, [0,1,2,3,4])

        ## Set pin0, pin3 and pin4 to digital high, others to digital low
        await dev.DO_writeValuePins(port_DO, [0,1,2,3,4], [1,0,0,1,1]) 

        ## Open pin4, pin5, pin6 and pin7 in port 1 with digital input 
        await dev.DI_openPins(port_DI, [4,5,6,7])

        ## Get pinmode from port 0 to port 3
        for i in range(4):
            pin_mode_status = await dev.sys_getPinModeInPort(i)
            print(f'pins: {pin_mode_status[0]}, slot{i}, mode {pin_mode_status[1]}') 
            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)

        ## Wait for 1 seconds
        await asyncio.sleep(1)  ## delay(second)

        ## Set port 0 to idle
        await dev.sys_setPortIdle(0)
        print()
        print("====================")
                
        ## Get pinmode from port 0 to port 3
        for i in range(4):
            pin_mode_status = await dev.sys_getPinModeInPort(i)
            print(f'pins: {pin_mode_status[0]}, slot{i}, mode {pin_mode_status[1]}') 
            ## Wait for 0.5 seconds
            await asyncio.sleep(0.5)  ## delay(second)

    except Exception as err:
        pywpc.printGenericError(err)
 
    ## Close pin0, pin1, pin2, pin3 and pin4 in port 0 with digital output 
    await dev.DO_closePins(port_DO, [0,1,2,3,4])

    ## Close pin4, pin5, pin6 and pin7 in port 1 with digital input
    await dev.DI_closePins(port_DI, [4,5,6,7])
    
    ## Disconnect network device
    dev.disconnect()
    
    ## Release device handle
    dev.close()
    
    print("End example code...")
    return

if __name__ == '__main__':
    asyncio.run(main())
