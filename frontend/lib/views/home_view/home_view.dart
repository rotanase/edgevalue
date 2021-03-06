import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/layout_template.dart';
import 'package:edgevalue/widgets/custom_raised_button.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:provider_architecture/provider_architecture.dart';
import 'package:edgevalue/viewmodels/home_view_model.dart';

import 'navigation_bar.dart';
import 'logo.dart';
import 'search_bar.dart';

class HomeView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print('HomeView Builder');
    return ViewModelProvider<HomeViewModel>.withConsumer(
      viewModelBuilder: () => HomeViewModel(),
      builder: (context, model, child) { print('HomeView with Model Builder');  return LayoutTemplate(
        navigationBar: NavigationBar(),
        body: Container(
          constraints: BoxConstraints(maxHeight: 500),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Logo(),
                SizedBox(height: 25),
                SearchBar(controller: model.controller),
                SizedBox(height: 18),
                CustomRaisedButton(
                  text: Translations.of(context).text('home_search_button_text'),
                  onPressed: () { model.navigateToCompanyView(); },
                ),
              ],
            ),
          ),
        ),
      );},
    );
  }
}
