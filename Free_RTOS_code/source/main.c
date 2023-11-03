#include <Arduino.h>
#include "FreeRTOS.h"
#include "os_task.h"

// Define the LED pin numbers
#define LED1_PIN 2
#define LED2_PIN 3

// Define the task delay in milliseconds
#define TASK_DELAY_MS 500

// Task function to blink LED1
void vTask1(void *pvParameters)
{
    pinMode(LED1_PIN, OUTPUT);
    for (;;)
    {
        digitalWrite(LED1_PIN, HIGH);
        vTaskDelay(TASK_DELAY_MS / portTICK_PERIOD_MS);
        digitalWrite(LED1_PIN, LOW);
        vTaskDelay(TASK_DELAY_MS / portTICK_PERIOD_MS);
    }
}

// Task function to blink LED2
void vTask2(void *pvParameters)
{
    pinMode(LED2_PIN, OUTPUT);
    for (;;)
    {
        digitalWrite(LED2_PIN, HIGH);
        vTaskDelay(TASK_DELAY_MS / portTICK_PERIOD_MS);
        digitalWrite(LED2_PIN, LOW);
        vTaskDelay(TASK_DELAY_MS / portTICK_PERIOD_MS);
    }
}

void setup()
{
    // Start the serial communication
    Serial.begin(9600);

    // Create task handles
    TaskHandle_t task1_handle;
    TaskHandle_t task2_handle;

    // Create task1 to blink LED1
    xTaskCreate(vTask1, "Task1", configMINIMAL_STACK_SIZE, NULL, 1, &task1_handle);

    // Create task2 to blink LED2
    xTaskCreate(vTask2, "Task2", configMINIMAL_STACK_SIZE, NULL, 1, &task2_handle);

    // Start the scheduler
    vTaskStartScheduler();
}

void loop()
{
    // Empty loop
}
