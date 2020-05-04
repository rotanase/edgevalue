import 'package:edgevalue/views/company_view/company_view.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/views/home_view/home_view.dart';
import 'package:edgevalue/locator.dart';

void main() {
  setupLocator();
  runApp(EdgeValue());
}

class EdgeValue extends StatefulWidget {
  @override
  _EdgeValueState createState() => _EdgeValueState();
}

class _EdgeValueState extends State<EdgeValue> {
  @override
  Widget build(BuildContext context) => MaterialApp(
    title: 'Edge Value',
    localizationsDelegates: [
      const TranslationsDelegate(),
      GlobalMaterialLocalizations.delegate,
      GlobalWidgetsLocalizations.delegate,
    ],
    supportedLocales: [
      const Locale('en', ''),
      const Locale('ro', ''),
    ],
    initialRoute: '/',
    routes: {
      '/': (context) => HomeView(),
      '/company': (context) => CompanyView(),
    },
  );
}
