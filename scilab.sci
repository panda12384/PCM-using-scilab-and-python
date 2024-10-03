clc ;
close ;
clear ;
f =2;
fs =20*f ; 
t =0:1/fs:2;
a =2;

msg = a*sin(2.*%pi*f*t);
subplot(3,1,1);
plot(t,msg)
xlabel('TIME');
ylabel('AMPLITUDE');
title('Message Signal');

x1 = msg + a; 
disp(x1,'Discrete Sampled Values of Message Signal');

quant = round (x1); 
disp(quant,'Quantized Sampled Values') ; 
enco = dec2bin(quant); 
disp(enco,'PCM coded Values') ; 

deco = bin2dec(enco); 
recover = deco - a ;
subplot(3,1,2) ;
plot(t,recover)
xlabel('TIME');
ylabel('AMPLITUDE');
title('Recovered Signal');
h = gca();
h.data_bounds =[0,-3;2,3]
subplot(3,1,3) ;
plot (t,msg,'b',t,recover,'r') ;
xlabel('TIME');
ylabel('AMPLITUDE');
title('Recovered VS Original Signal') ;
h = gca() ;
h.data_bounds =[0,-3;2,3]
