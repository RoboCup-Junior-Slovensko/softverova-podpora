#define MAX_DLZKA_PAKETU 10

// pakety v oboch smeroch zacinaju znakom '$' a koncia znakom '\n'

uint8_t paket[MAX_DLZKA_PAKETU];
uint8_t *p;
uint8_t citam;

void setup() 
{
  Serial.begin(115200);
  p = paket;
  citam = 0;
  Serial.println("$init");
}

void spracuj_paket()
{
  // na tomto mieste mame v poli paket[] prijaty 0-ukonceny retazec znakov
  int a;
  // v tejto ukazke retazec dekodujeme ako cislo a vypiseme spravu s dvojnasobkom
  // vo vasom pripade budete na tomto mieste reagovat na spravu podla potreby...
  sscanf((char *)paket, "%d", &a);
  Serial.print("$dvojnasobok je ");
  Serial.println(a * 2);
}

void precitaj_dalsi_znak()
{
  if (p - paket >= MAX_DLZKA_PAKETU) p = paket;
  
  *p = Serial.read();
  if (*p == '$') 
  {
    p = paket;
    citam = 1;
  }
  else if (citam)
  {
    if (*p != '\n') p++;
    else 
    {
      *p = 0;
      citam = 0;
      spracuj_paket();
      p = paket;
    }
  }
}

void loop() 
{
  if (Serial.available()) precitaj_dalsi_znak();
  if (millis() % 4000 == 0) 
  {
    Serial.print("$arduino zdravi kazde 4 sekundy\n");
    delay(1);
  }
}
