import 'package:edgevalue/viewmodels/company_view_model.dart';
import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/layout_template.dart';
import 'package:provider_architecture/provider_architecture.dart';

import 'navigation_bar.dart';

class CompanyView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print('CompanyView Builder');
    return ViewModelProvider<CompanyViewModel>.withConsumer(
      viewModelBuilder: () => CompanyViewModel(),
      onModelReady: (model) => model.getCompanyByUri(
        ModalRoute.of(context).settings.name
      ),
      builder: (context, model, child) {  print('CompanyView with Model Builder'); return LayoutTemplate(
        navigationBar: NavigationBar(),
        body: Center(
          child: model?.companyName == null
            ? CircularProgressIndicator()
            : Text(
              model.companyName,
              style: TextStyle(fontSize: 40),
            ),
        ),
      );}
    );
  }
}
