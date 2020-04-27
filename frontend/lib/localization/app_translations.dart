import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;

import 'dart:async';
import 'dart:convert';

class Translations {
  Translations(Locale locale) {
    this.locale = locale;
    _localizedValues = null;
  }

  Locale locale;
  static Map<dynamic, dynamic> _localizedValues;

  static Translations of(BuildContext context) {
    return Localizations.of<Translations>(context, Translations);
  }

  String text(String key) {
    return _localizedValues[key] ?? '** $key not found';
  }

  static Future<Translations> load(Locale locale) async {
    Translations translations = new Translations(locale);
    String jsonContent = await rootBundle.loadString("locale/i18n_${locale.languageCode}.json");
    _localizedValues = json.decode(jsonContent);
    return translations;
  }

  get currentLanguage => locale.languageCode;
}

class TranslationsDelegate extends LocalizationsDelegate<Translations> {
  const TranslationsDelegate();

  @override
  bool isSupported(Locale locale) => ['en','ro'].contains(locale.languageCode);

  // Temporary app language can only be modified here, replace `locale`
  // with `Locale('en')` or `Locale('ro')`.
  @override
  Future<Translations> load(Locale locale) => Translations.load(Locale('ro')/* replace here */);

  @override
  bool shouldReload(TranslationsDelegate old) => false;
}