#include <LedControl.h>

int DIN = 10;
int CS =  9;
int CLK = 8;

LedControl lc = LedControl(DIN,CLK,CS,4);

void setup() {

lc.shutdown(1,false);      
lc.setIntensity(1,1);      
lc.clearDisplay(1);  
lc.shutdown(2,false);      
lc.setIntensity(2,1);      
lc.clearDisplay(2);
lc.shutdown(0,false);      
lc.setIntensity(0,1);      
lc.clearDisplay(0);  
lc.shutdown(3,false);      
lc.setIntensity(3,1);      
lc.clearDisplay(3);

}

void loop() {

byte left_eye_and_right_eye_board1[8]={0x7E,0x81,0x81,0x99,0x99,0x81,0x81,0x7E};

byte small_to_big_matrix2_board1[8]={0xFE,0x1,0x1,0x19,0x19,0x1,0x1,0xFE};
byte small_to_big_matrix3_board1[8]={0x0,0x1,0x1,0x1,0x1,0x1,0x1,0x0};
byte small_to_big_matrix1_board1[8]={0x7F,0x80,0x80,0x98,0x98,0x80,0x80,0x7F};
byte small_to_big_matrix0_board1[8]={0x0,0x80,0x80,0x80,0x80,0x80,0x80,0x0};


byte left_eye_matrix3_board1[8]  = {0x1,0x2,0x2,0x2,0x2,0x2,0x2,0x1};
byte left_eye_matrix2_board1[8]  = {0xFE,0x1,0x31,0x49,0x49,0x31,0x1,0xFE};
byte right_eye_matrix1_board1[8] = {0x7F,0x80,0x8C,0x92,0x92,0x8C,0x80,0x7F};
byte right_eye_matrix0_board1[8] = {0x80,0x40,0x40,0x40,0x40,0x40,0x40,0x80};

//this is for small eyes---------------------------
SmallEyes(left_eye_and_right_eye_board1);

//this is the transision---------------------------
BigToSmall(small_to_big_matrix3_board1,small_to_big_matrix2_board1,small_to_big_matrix1_board1,small_to_big_matrix0_board1);

//this is for big eyes-----------------------------
BigEyes(left_eye_matrix3_board1,left_eye_matrix2_board1,right_eye_matrix1_board1,right_eye_matrix0_board1);

//this is for the transistion again----------------
BigToSmall(small_to_big_matrix3_board1,small_to_big_matrix2_board1,small_to_big_matrix1_board1,small_to_big_matrix0_board1);

//clearing the 3rd (last) and 0th (first) matrix so it becomes smooth
lc.clearDisplay(3);
lc.clearDisplay(0);
}

void SmallEyes(byte left_eye_and_right_eye[]){
  for(int i=0;i<8;i++)
  {
    lc.setRow(2,i,left_eye_and_right_eye[i]);
    lc.setRow(1,i,left_eye_and_right_eye[i]);
  }
  delay(1000);
}

void BigToSmall(byte small_to_big_matrix3[],byte small_to_big_matrix2[],byte small_to_big_matrix1[],byte small_to_big_matrix0[]){
  for(int i=0;i<8;i++)
  {
    lc.setRow(3,i,small_to_big_matrix3[i]);
    lc.setRow(2,i,small_to_big_matrix2[i]);
    lc.setRow(1,i,small_to_big_matrix1[i]);
    lc.setRow(0,i,small_to_big_matrix0[i]);
  }
  delay(100);
 
}

void BigEyes(byte left_eye_matrix3[],byte left_eye_matrix2[],byte right_eye_matrix1[],byte right_eye_matrix0[]) {

  for(int i=0;i<8;i++)
  {
    lc.setRow(3,i,left_eye_matrix3[i]);
    lc.setRow(2,i,left_eye_matrix2[i]);
    lc.setRow(1,i,right_eye_matrix1[i]);
    lc.setRow(0,i,right_eye_matrix0[i]);
  }
  delay(2000);
}
