import six
from google.cloud import translate_v2 as translate


def translate_text(text, target):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))


def list_languages():
    """Lists all available languages."""
    translate_client = translate.Client()

    results = translate_client.get_languages()

    for language in results:
        print("{name} ({language})".format(**language))


def list_languages_with_target(target):
    """Lists all available languages and localizes them to the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    results = translate_client.get_languages(target_language=target)

    for language in results:
        print("{name} ({language})".format(**language))


if __name__ == "__main__":
    # list_languages()
    # list_languages_with_target('en')
    translate_text("good job", "de")
