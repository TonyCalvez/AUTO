function draw(x,u)
alpha = 1; beta = 1; L = 3; l = 2;
v = x(4); delta = x(5);

M = [-L/2 L/2 L/2 -L/2 -L/2;
     -l/2 -l/2 l/2 l/2  -l/2;
     1    1   1   1    1];

M_roue = [-0.2 0.2;
          0 0;
          1 1];
       
M_arrd = [1 0 -L/2;
          0 0 -l/2-0.1;
          0 0 1] * M_roue;

M_av = [cos(delta) -sin(delta) +L/2;
          sin(delta) cos(delta) 0;
          0 0 1]*M_roue;
      
M_arrg = [1 0 -L/2;
          0 0 +l/2+0.1;
          0 0 1] * M_roue;

R = [cos(x(3)) -sin(x(3)) x(1);
     sin(x(3)) cos(x(3)) x(2);
     0 0 1];
 
M=R*M; M_arrd=R*M_arrd; M_arrg=R*M_arrg; M_av=R*M_av;
    
plot(M(1,:),M(2,:),'b');
plot(M_arrd(1,:),M_arrd(2,:),'b');
plot(M_arrg(1,:),M_arrg(2,:),'b');
plot(M_av(1,:),M_av(2,:),'b');
end    