FROM php:7.4-fpm

ADD ./php/www.conf /usr/local/etc/php-fpm.d/www.conf

COPY /php/php.ini-production /usr/local/etc/php/conf.d/php.ini

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libzip-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    && docker-php-ext-install pdo pdo_mysql \ 
    && docker-php-ext-install exif \
    && docker-php-ext-install zip \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd

RUN groupadd laravel && useradd -g laravel laravel

RUN mkdir -p /var/www

RUN chown laravel:laravel /var/www

WORKDIR /var/www