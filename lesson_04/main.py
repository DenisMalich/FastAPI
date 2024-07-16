

import argparse
from downloader import download_images
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Программа для скачивания изображений с заданных URL-адресов.")
    parser.add_argument('urls', metavar='URL', type=str, nargs='*',
                        help='Список URL-адресов изображений для скачивания (опционально)')
    args = parser.parse_args()

    if args.urls:
        urls = args.urls
    else:
        urls = []

    # Интерактивный режим для ввода URL-адресов, если они не были переданы через аргументы командной строки
    while True:
        url = input(
            "Введите URL-адрес изображения (или 'готово' для завершения ввода): ").strip()
        if url.lower() == 'готово':
            break
        urls.append(url)

    if not urls:
        print("Нет URL-адресов для скачивания.")
        sys.exit(0)

    download_images(urls)


if __name__ == "__main__":
    main()
