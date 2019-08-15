import argparse
import logging
import tensorflow as tf


def main(args):
    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    # character length： a array represent a Chinese Character, 
    # stroke(30) + pinyin(additional number represented tone)(7) + punctuation(1) + any position placeholder(3) + padding
    parser.add_argument('--character_length', type=int, default=40, help='The length of array representing character')
    parser.add_argument('--embedding_length', type=int, default=20, help='The length of character Embedding')

    args = parser.parse_args()
    main(args)