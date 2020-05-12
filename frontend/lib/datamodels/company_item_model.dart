import 'package:flutter/material.dart';

class CompanyItemModel extends StatefulWidget {
  final int id;
  final String name, ticker, isin;
  final Color color, selectedColor;

  // Store the state of the `CompanyItemModel`.
  _CompanyItemModelState _state;

  CompanyItemModel({
    this.id,
    this.name = '',
    this.ticker = '',
    this.isin = '',
    this.color = Colors.white,
    this.selectedColor = const Color(0xFFE0E0E0), // grey[300]
  });

  CompanyItemModel.fromJson(Map<String, dynamic> map) : this(
    id: map['id'],
    name: map['name'],
    ticker: map['ticker'],
    isin: map['isin'],
  );

  bool matches(String pattern) {
    pattern = pattern.toLowerCase();
    return name.toLowerCase().contains(pattern) ||
      ticker.toLowerCase().contains(pattern) ||
      isin.toLowerCase().contains(pattern);
  }

  @override
  _CompanyItemModelState createState() => _state = _CompanyItemModelState();

  // TODO: Do not use a mutable object `_state` for this, find a better way
  // Hack: This is temporary, it offers the posibility to mark as selected
  // an item, by using down/up arrow key on the keyboard.
  bool get isSelected => _state._isSelected;
  void setSelected(bool selected) { _state.setState(() { _state._isSelected = selected; }); }
  void Function() resetAllSelected;
}

class _CompanyItemModelState extends State<CompanyItemModel> {
  bool _isSelected = false;

  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onHover: (_) { widget?.resetAllSelected(); setState(() { _isSelected = true; }); },
      onEnter: (_) { widget?.resetAllSelected(); setState(() { _isSelected = true; }); },
      onExit: (_) { widget?.resetAllSelected(); setState(() { _isSelected = false; }); },
      child: Ink(
        color: _isSelected ? widget.selectedColor : widget.color,
        child: ListTile(
          title: Text(widget.name),
          subtitle: Text('Ticker: ${widget.ticker} / ISIN: ${widget.isin}'),
        ),
      ),
    );
  }
}
