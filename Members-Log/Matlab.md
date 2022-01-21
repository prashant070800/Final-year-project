clc



close all

a=imread('Capture1.jpg');

b=rgb2gray(a);

subplot(2,2,1);

imshow(b);

title('Ajeet');

subplot(2,2,3);

imhist(b);

title('Histogram Deepankar');

j=histeq(b);

subplot(2,2,2);

imshow(j);

title('Image after histogram equalization Chitransh');

subplot(2,2,4);

imhist(j);

title('Histogram of Image after histogram equalization');
