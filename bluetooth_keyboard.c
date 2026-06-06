#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int get_input(){
    //receive/parse bluetooth input here
    return rand() % 5; //get a random integer between 0 and 4
}

void press_key(WORD vk) {
    INPUT inputs[2] = {0};

    //press key
    inputs[0].type = INPUT_KEYBOARD;
    inputs[0].ki.wVk = vk;

    //release key
    inputs[1].type = INPUT_KEYBOARD;
    inputs[1].ki.wVk = vk;
    inputs[1].ki.dwFlags = KEYEVENTF_KEYUP;

    //send command
    SendInput(2, inputs, sizeof(INPUT));
}

void main(void) {
    int input = get_input();
    printf("Focus the target window. Typing starts in 5 seconds...\n");
    Sleep(5000);
    
    int i = 0;
    while(i < 20){
        if (input == 0){
            press_key('A');
        }else if (input == 1){
            press_key('B');
        }else if (input == 2){
            press_key('C');
        }else if (input == 3){
            press_key('D');
        }else if (input == 4){
            press_key('E');
        }
        input = get_input();
        i++;
    }
}