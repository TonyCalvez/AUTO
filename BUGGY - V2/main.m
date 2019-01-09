% Global variables to share with other files.
global u;
global bExit;
global scale;

button = questdlg('Welcome to Ecrazor game. Activate sound?', 'Ecrazor game');
if (strcmp(button, 'Yes') == 1)
    sound(audioread('sound.wav'), 22050);%wavplay(wavread('sound.wav'), 22050, 'async');
end

button = questdlg('Get the most of targets within the shortest time. Controls are z,s,q,d keys, zoom with +,- and stop with ESC. Ready?', 'Ready?');
if (strcmp(button, 'Yes') == 0)
    return;
end

% Create a figure that will use the function keycontrol() when a key is
% pressed.
fig = figure('Position',[200 200 400 400],'KeyPressFcn','keycontrol','Name','Ecrazor game','NumberTitle','off');
% Force the figure to have input focus (required to capture keys).
set(fig,'WindowStyle','Modal');
axis('off');

bExit = 0;
scale = 50;

x = [0;0;0]; %Initialiser avec une dimension 3, pour être conforme au comportement défini dans f.m
u = [0;0];
dt = 0.01;
t = 0;
    
targets = 0;
target = scale*rand(2,1);

while (bExit == 0)
    x=x+f(x,u);  
    clf;
    hold on;
    axis([-scale,scale,-scale,scale]); axis square;
    draw(x,u);
    
    plot(target(1),target(2),'--rs','LineWidth',5,'MarkerSize',5);    
    if ((target(1)-2.5 < x(1))&&(x(1) < target(1)+2.5)&&(target(2)-2.5 < x(2))&&(x(2) < target(2)+2.5))
        targets = targets+1;
        target = scale*rand(2,1);
    end
    
    % Wait a little bit.
    pause(dt);
    t = t+dt;
end

targets
t
score = 100*targets/t

str = sprintf('Targets catched : %d, total time = %f s, score = %6.f', targets, t, score);
warndlg(str, 'Results');

close(fig);

