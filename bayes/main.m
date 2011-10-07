data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);

test_data = [data1; data2];
figure;
hold on;

plot(data2(:,1), data2(:,2), '.');
plot(data1(:,1), data1(:,2), '.r');
legend('Hand holding book', 'Hand');
xlabel('green');
ylabel('red');

% Plot confidence interval
[mu sigma] = bayes(test_data)
theta = [0:0.01:2*pi];

x1 = 2*sigma(1,1)*cos(theta) + mu(1,1);
y1 = 2*sigma(1,2)*sin(theta) + mu(1,2);
x2 = 2*sigma(2,1)*cos(theta) + mu(2,1);
y2 = 2*sigma(2,2)*sin(theta) + mu(2,2);

plot(x1, y1, 'r');
plot(x2, y2);

% Training! \o/
[M N] = size(test_data);
p = prior(test_data);
g = discriminant(test_data(:, 1:2), mu, sigma, p);
[dummy class] = max(g, [], 2);
class = class - 1;
error_test = 1.0 - sum(class == test_data(:,end))/M

% Overlaying the decision boundary?
ax = [0.2 0.5 0.2 0.45];
axis(ax);
x = ax(1):0.01:ax(2);
y = ax(3):0.01:ax(4);
[z1 z2] = meshgrid(x, y);
z1 = reshape(z1, size(z1, 1)*size(z1, 2), 1);
z2 = reshape(z2, size(z2, 1)*size(z2, 2), 1);
g = discriminant([z1 z2], mu, sigma, p);
gg = g(:,1) - g(:,2);
gg = reshape(gg, length(y), length(x));
[c,h] = contour(x, y, gg, [0.0 0.0]);
set(h, 'LineWidth', 3);