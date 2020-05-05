import 'package:flutter/material.dart';

class CompanyItemModel extends StatefulWidget {
  CompanyItemModel({
    this.id,
    this.name = '',
    this.ticker = '',
    this.isin = '',
    this.color = Colors.white,
    this.hoverColor = const Color(0xFFE0E0E0), // grey[300]
  });

  CompanyItemModel.fromJson(Map<String, dynamic> map) : this(
    id: map['id'],
    name: map['name'],
    ticker: map['ticker'],
    isin: map['isin'],
  );

  final int id;
  final String name, ticker, isin;
  final Color color, hoverColor;

  bool matches(String pattern) {
    pattern = pattern.toLowerCase();
    return name.toLowerCase().contains(pattern) ||
      ticker.toLowerCase().contains(pattern) ||
      isin.toLowerCase().contains(pattern);
  }

  @override
  _CompanyItemModelState createState() => _CompanyItemModelState();
}

class _CompanyItemModelState extends State<CompanyItemModel> {
  Color _currentColor;

  void _updateCurrentColor(bool mouseHover) {
    setState(() {
      _currentColor = mouseHover ? widget.hoverColor : widget.color;
    });
  }

  @override
  void initState() {
    super.initState();
    _currentColor = widget.color;
  }

  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onEnter: (_) { _updateCurrentColor(true); },
      onExit: (_) { _updateCurrentColor(false); },
      child: Ink(
        color: _currentColor,
        child: ListTile(
          title: Text(widget.name),
          subtitle: Text('Ticker: ${widget.ticker} / ISIN: ${widget.isin}'),
        ),
      ),
    );
  }
}
