% Global variables to share with other files.
global u;
global bExit;
global scale, global offsetx, global offsety;
global L, global l, global alpha, global alphafx, global alphafy, global beta;

% Controls are z,s,q,d keys, zoom with +,-, move camera with i,j,k,l and stop with ESC.

% Create a figure that will use the function keycontrol() when a key is
% pressed.
fig = figure('Position',[200 200 400 400],'KeyPressFcn','keycontrol','Name','Motorboat simu','NumberTitle','off');
% Force the figure to have input focus (required to capture keys).
set(fig,'WindowStyle','Modal');
axis('off');

bExit = 0;
scale = 5; offsetx = 0; offsety = 0;

L = 1.22; % Length of the hull (in m).
l = 0.35; % Width of the hull (in m).
alpha = 2.0; % Coefficient a regler en regardant la vitesse du bateau pour une entree u(1) donnee.
alphafx = 1.0; % Coefficient a regler pour les frottements.
alphafy = 1.0; % Coefficient a regler pour les frottements.
beta = 0.7; % Coeffecient (en rad) a regler selon l'angle max du jet.

x = [0;0;0;0];
zk = [x(1); x(2); x(4)]; Gk = diag([0.1,0.1,0.1]);
Galphak = diag([0.001,0.001,0.001]); 
Gk=diag([0.0001,0.0001,0.0001]); % Corresponding covariance matrix (error of the initial position).
 
u = [0;0];
dt = 0.05;
t = 0;

target = scale*(1-2*rand(2,1)); % Randomly initialize first waypoint.

while (bExit == 0)
    % Simulated state evolution.
    x = x+f(x,u)*dt;
    
    % Kalman filter known inputs.
    % Kalman filter evolution matrix.
    Ak = [1 , 0, dt*cos(beta*u(2))*cos(x(3)); 
        0 , 1, dt*cos(beta*u(2))*sin(x(3));
        0, 0 , 1-dt*alphafx]; 
    Uk = [0;0;dt*alpha*u(1)];

    % Kalman filter measurements.
%     yk = [];
%     Gbetak = [];
%     Ck = [];
    yk = [x(4)]; Ck=[0 0 1]; Gbetak = 0.00001;  
       
    
    % Computations with the Kalman filter.
    [zk,Gk,zkup,Gzkup]=kalman(zk,Gk,Uk,yk,Galphak,Gbetak,Ak,Ck);
    
    
    % Autonomous control part to go to waypoints.
     v_bar=0.5;
     
    theta_bar = atan2(target(2)-zkup(2),target(1)-zkup(1));    
    if (cos(x(3)-theta_bar) > 0.5)
        u(2) = -sin(x(3)-theta_bar);
    else
        u(2)= -sign(sin((x(3)-theta_bar)));
    end    
    
    clf;
    hold on;
    axis([-scale+offsetx,scale+offsetx,-scale+offsety,scale+offsety]); axis square;
    draw(x,u);
    %Ellipse de confiance 
    draw_ellipse([zkup(1);zkup(2)],diag([Gzkup(1,1);Gzkup(2,2)]),0.95);

    % Draw current waypoint and change it when we are close.
    plot(target(1),target(2),'--rs','LineWidth',5,'MarkerSize',5);    
    if ((target(1)-2.5 < zkup(1))&(zkup(1) < target(1)+2.5)&(target(2)-2.5 < zkup(2))&(zkup(2) < target(2)+2.5))
        target = scale*(1-2*rand(2,1));
    end
    
    
    % Wait a little bit.
    pause(0.02); % <dt because there are also computations delays...
    t = t+dt;
end

close(fig);
