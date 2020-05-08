import 'package:edgevalue/viewmodels/company_view_model.dart';
import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/layout_template.dart';
import 'package:provider_architecture/provider_architecture.dart';

import 'navigation_bar.dart';

class CompanyView extends StatelessWidget {
  final int companyId;

  const CompanyView({Key key, @required this.companyId}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ViewModelProvider<CompanyViewModel>.withConsumer(
      viewModelBuilder: () => CompanyViewModel(),
      onModelReady: (model) => model.getCompanyData(companyId),
      builder: (context, model, child) => LayoutTemplate(
        navigationBar: NavigationBar(),
        body: Center(
          child: model?.companyName == null
            ? CircularProgressIndicator()
            : Text(
              model.companyName,
              style: TextStyle(fontSize: 40),
            ),
        ),
      ),
    );
  }
}
