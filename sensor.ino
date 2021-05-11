
///////////////////////////////////////////////////////
/* CO2 값을 읽고 라즈베리파이에 UART통신으로 데이터를 보내주는 코드*/
///////////////////////////////////////////////////////


/************************Hardware Related Macros************************************/
#define         MG_PIN                       (A7)     //아날로그 값을 입력받을 핀을 정의 
#define         BOOL_PIN                     (50)    //디지털값을 입력받을 핀을 정의
#define         DC_GAIN                      (8.5)   //증폭회로의 전압이득 정의(변경 X)

 /***********************Software Related Macros************************************/

#define         READ_SAMPLE_INTERVAL         (50)    //샘플 값 추출 간격
#define         READ_SAMPLE_TIMES            (5)     //추출할 샘플값의 갯수 
                                                    //추출할 샘플값들의 평균값이 측정값입니다.

/**********************Application Related Macros**********************************/
//These two values differ from sensor to sensor. user should derermine this value.
#define         ZERO_POINT_VOLTAGE           (0.324) //이산화 탄소가 400ppm일때의 전압값 (수정 X)
#define         REACTION_VOLTGAE             (0.020) //이산화 탄소가 1000ppm일때의 전압값(수정 X)

/*****************************Globals***********************************************/
float           CO2Curve[3]  =  {2.602,ZERO_POINT_VOLTAGE,(REACTION_VOLTGAE/(2.602-3))};   
                                                     //위의 두 값들은 곡선위에 존제합니다.
                                                     //이 두점에서 라인이 생성이 되는데,
                                                     //원래의 곡선과 가깝습니다.
                                                     //번역된 부분으로 읽는데 잘 파악이 되지는 않네요, 센서값 곡선 그래프에 맞추어 계산을 하기 위한 설정값들이라고 생각하면 될듯합니다.
                                                     //data format:{ x, y, slope}; point1: (lg400, 0.324), point2: (lg4000, 0.280) 
                                                     //slope = ( reaction voltage ) / (log400 –log1000) 

#include <MsTimer2.h>

// R2868A센서 핀 넘버
const int flamePin = A3;
int val;
int sum=0;
unsigned long time;
// 부저 핀 넘버
const int buzzer = A4;

// LED 핀 넘버 
const int R = 31;
const int G = 33;
const int B = 35; 
 
void setup() {
    // LED상태 설정
    pinMode(R, OUTPUT);
    pinMode(G, OUTPUT);
    pinMode(B, OUTPUT);             

    // 시리얼0번으로 통신하기 때문에 Serial.println은 사용 불가
    Serial.begin(9600);                              //UART setup, baudrate = 9600bps
    pinMode(BOOL_PIN, INPUT);                        //set pin to input
    digitalWrite(BOOL_PIN, HIGH);                    //turn on pullup resistors
    //Serial.print("MG-811 Demostration\n"); 
   
}
void loop() {
    int percentage;
    float volts; 

    volts = MGRead(MG_PIN);
    //Serial.print( "SEN0159:" );
    //Serial.print(volts); 
    //Serial.print( "V           " );
  
    percentage = MGGetPercentage(volts,CO2Curve);
    //Serial.print("CO2:");
    if (percentage == -1) {
        Serial.print( "a<400" );
    } else {
        Serial.print("a"+percentage);
    }
    //Serial.print( "ppm" );  
    //Serial.print( "       Time point:" );
    //Serial.print(millis());

    //Serial.print("\n");
    
    //수치에 따라 led 색 제어
    if(400<percentage<600){
       digitalWrite(B,HIGH);
       delay(3000);
       digitalWrite(B,LOW);      
    }
    if(600<percentage<800){
       digitalWrite(G,HIGH);
       delay(3000);
       digitalWrite(G,LOW);
    }
    if (800<percentage){
       digitalWrite(R,HIGH);
       delay(3000);
       digitalWrite(R,LOW);       
    }
    
    if (digitalRead(BOOL_PIN) ){
        //Serial.print( "=====BOOL is HIGH======" );
    } else {
        //Serial.print( "=====BOOL is LOW======" );
    }
    //Serial.print("\n"); 

   val=analogRead(flamePin);
   noTone(buzzer);
   time = millis();
   //5초이상 불꽃 감지시 부저 울리기
   if(val!=0){
      sum++;
    }
    if(val==0){
      sum=0;
    }
    if(time%5000<1000&&sum>=5){
      tone(buzzer, 500, 100);
      
    }

  
   

   delay(1000);
}



/*****************************  MGRead *********************************************
Input:   mg_pin - analog channel
Output:  output of SEN-000007
Remarks: This function reads the output of SEN-000007
************************************************************************************/

float MGRead(int mg_pin) {
    int i;
    float v=0;
 
    for (i=0;i<READ_SAMPLE_TIMES;i++) {
        v += analogRead(mg_pin);
        delay(READ_SAMPLE_INTERVAL);
    }
    v = (v/READ_SAMPLE_TIMES) *5/1024 ;
    return v;  
}


/*****************************  MQGetPercentage **********************************
Input:   volts   - SEN-000007 output measured in volts
         pcurve  - pointer to the curve of the target gas
Output:  ppm of the target gas
Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm) 
         of the line could be derived if y(MG-811 output) is provided. As it is a 
         logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic 
         value.
************************************************************************************/

int  MGGetPercentage(float volts, float *pcurve) {
   if ((volts/DC_GAIN )>=ZERO_POINT_VOLTAGE) {
      return -1;
   } else { 
      return pow(10, ((volts/DC_GAIN)-pcurve[1])/pcurve[2]+pcurve[0]);
   }
}
