#pragma once
#include <Arduino.h>

constexpr uint8_t PIN_STATUS_LED = 2;
constexpr uint8_t PIN_OLED_DC = 4;
constexpr uint8_t PIN_OLED_CS = 5;
constexpr uint8_t PIN_OLED_RST = -1; // Assuming connected to EN/RST

constexpr uint8_t PIN_RELAY_CTRL = 12;
constexpr uint8_t PIN_MUTE_ALL = 13;

constexpr uint8_t PIN_IR_RECV = 14;
constexpr uint8_t PIN_ENC_A = 15;
constexpr uint8_t PIN_ENC_B = 16;
constexpr uint8_t PIN_ENC_SW = 17;

constexpr uint8_t PIN_SPI_SCK = 18;
constexpr uint8_t PIN_SPI_MISO = 19;
constexpr uint8_t PIN_SPI_MOSI = 23;

constexpr uint8_t PIN_VOL_CS = 25;
constexpr uint8_t PIN_MUX_A = 26;
constexpr uint8_t PIN_MUX_B = 27;

constexpr uint8_t PIN_FAULT1 = 32;
constexpr uint8_t PIN_FAULT2 = 33;
constexpr uint8_t PIN_FAULT3 = 34;

constexpr uint8_t PIN_NTC_ADC = 35;
constexpr uint8_t PIN_DC_OFFSET_ADC = 36;

constexpr uint8_t PIN_BT_KEY = 21;

constexpr uint8_t PIN_UART_TX = 1;
constexpr uint8_t PIN_UART_RX = 3;

constexpr uint32_t SPI_SPEED_OLED = 8000000;
constexpr uint32_t SPI_SPEED_MCP4252 = 1000000;
