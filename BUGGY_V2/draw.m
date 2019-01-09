function draw(x,u)
alpha = 1;beta = 1;L = 1;l = 0.5;
v = alpha * u(1); delta = beta * u(2);

M = [-L/2 L/2 L/2 -L/2 -L/2;
     -l/2 -l/2 l/2 l/2  -l/2;
     1    1   1   1    1];

M_roue = [-0.2 0.2;
          0 0;
          1 1];
       
M_arrd = [1 0 -L/2;
          0 0 -l/2-0.1;
          0 0 1] * M_roue;

M_avg = [cos(delta) -sin(delta) +L/2;
          sin(delta) cos(delta) +l/2+0.1;
          0 0 1]*M_roue;
      
M_arrg = [1 0 -L/2;
          0 0 +l/2+0.1;
          0 0 1] * M_roue;
      
M_avd = [cos(delta) -sin(delta) +L/2;
          sin(delta) cos(delta) -l/2-0.1;
          0 0 1]*M_roue;

R = [cos(x(3)) -sin(x(3)) x(1);
     sin(x(3)) cos(x(3)) x(2);
     0 0 1];
 
M=R*M; M_arrd=R*M_arrd; M_arrg=R*M_arrg; M_avd=R*M_avd; M_avg=R*M_avg;
    
plot(M(1,:),M(2,:),'b');
plot(M_arrd(1,:),M_arrd(2,:),'b');
plot(M_arrg(1,:),M_arrg(2,:),'b');
plot(M_avd(1,:),M_avd(2,:),'b');
plot(M_avg(1,:),M_avg(2,:),'b');
end    