#include "ets_sys.h"
#include "osapi.h"
#include "gpio.h"
#include "os_type.h"
#include "user_config.h"
#include "user_interface.h"

#define user_procTaskPrio        0
#define user_procTaskQueueLen    1

//Allocate an "espconn"
pHTTPServer = (struct espconn *)os_zalloc(sizeof(struct espconn));
ets_memset( pHTTPServer, 0, sizeof( struct espconn ) );

//Initialize the ESPConn
espconn_create( pHTTPServer );
pHTTPServer->type = ESPCONN_TCP;
pHTTPServer->state = ESPCONN_NONE;

//Make it a TCP conention.
pHTTPServer->proto.tcp = (esp_tcp *)os_zalloc(sizeof(esp_tcp));
pHTTPServer->proto.tcp->local_port = 80;

//"httpserver_connectcb" gets called whenever you get an incoming connetion.
espconn_regist_connectcb(pHTTPServer, server_connectcb);

//Start listening!
espconn_accept(pHTTPServer);

//I don't know what default is, but I always set this.
espconn_regist_time(pHTTPServer, 15, 0);

os_event_t    user_procTaskQueue[user_procTaskQueueLen];
static void loop(os_event_t *events);

//Main code function
static void ICACHE_FLASH_ATTR
loop(os_event_t *events)
{
    os_printf("Hello\n\r");
    os_delay_us(10000);
    system_os_post(user_procTaskPrio, 0, 0 );
}

//Init function
void ICACHE_FLASH_ATTR
user_init()
{
    char ssid[32] = SSID;
    char password[64] = SSID_PASSWORD;
    struct station_config stationConf;

    //Set station mode
    wifi_set_opmode( 0x1 );

    //Set ap settings
    os_memcpy(&stationConf.ssid, ssid, 32);
    os_memcpy(&stationConf.password, password, 64);
    wifi_station_set_config(&stationConf);

    //Start os task
    system_os_task(loop, user_procTaskPrio,user_procTaskQueue, user_procTaskQueueLen);

    system_os_post(user_procTaskPrio, 0, 0 );
}
