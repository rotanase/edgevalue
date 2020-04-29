import 'package:flutter/material.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/widgets/search_bar/better_list_tile.dart';

class SearchBarDesktop extends StatefulWidget {
  @override
  _SearchBarDesktopState createState() => _SearchBarDesktopState();
}

class _SearchBarDesktopState extends State<SearchBarDesktop> {

  // An overlay in which search results are shown.
  OverlayEntry _overlayEntry;

  // Controller for the text field widget of this search bar.
  final TextEditingController _textEditingController = TextEditingController();

  // Focus node used to hide `_overlayEntry` when SearchBar looses focus.
  final FocusNode _focusNode = FocusNode();

  /*
   * This is a helper method, it creates an overlay entry
   * with search results for the `searchedString`. It is
   * called by _showSearchResults().
   */
  OverlayEntry _createOverlayEntry(String searchedString) {
    RenderBox rBox = context.findRenderObject();
    Offset rBoxOffset = rBox.localToGlobal(Offset.zero);
    Size rBoxSize = rBox.size;

    return OverlayEntry(
      builder: (context) => Positioned(
        left: rBoxOffset.dx,
        top: rBoxOffset.dy + rBoxSize.height + 5.0,
        width: rBoxSize.width * 1.5,
        child: Material(
          elevation: 4.0,
          child: ListView(
            padding: EdgeInsets.zero,
            shrinkWrap: true,
            children: <Widget>[
              BetterListTile(
                title: 'Banca Transilvania',
                subtitle: 'Simbol: TLV',
                secondSubtitle: 'ISIN: 1231242323',
                hoverColor: Colors.grey[300],
              ),
              BetterListTile(
                title: 'OMV Petrom',
                subtitle: 'Simbol: SNP',
                secondSubtitle: 'ISIN: 1231242323',
                hoverColor: Colors.grey[300],
              ),
              BetterListTile(
                title: 'Transgaz',
                subtitle: 'Simbol: SNG',
                secondSubtitle: 'ISIN: 1231242323',
                hoverColor: Colors.grey[300],
              ),
            ],
          ),
        ),
      ),
    );
  }

  /*
   * Helper function to remove _overlayEntry.
   * Always set it to null if you will delete it otherwise.
   */
  void _removeOverlayEntryIfPresent() {
    _overlayEntry?.remove();
    _overlayEntry = null;
  }

  void _showSearchResults(String tickerToSearch) {
    _removeOverlayEntryIfPresent();
    
    if (tickerToSearch?.isNotEmpty ?? false) {
      _overlayEntry = _createOverlayEntry(tickerToSearch);
      Overlay.of(context).insert(_overlayEntry);
    }
  }

  OutlineInputBorder _searchBarOutlineBoder() {
    return OutlineInputBorder(
      borderRadius: BorderRadius.circular(100),
      borderSide: BorderSide(
        color: Colors.grey[700],
        width: 0.5,
      ),
    );
  }

  @override
  void initState() {
    super.initState();
    _focusNode.addListener(() {
      if (_focusNode.hasFocus) {
        _showSearchResults(_textEditingController.text);
      } else {
        _removeOverlayEntryIfPresent();
      }
    });
  }

  @override
  void dispose() {
    _removeOverlayEntryIfPresent();
    _textEditingController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 30,
      width: 250,
      child: TextFormField(
        cursorColor: Colors.black,
        cursorWidth: 0.25,
        decoration: InputDecoration(
          contentPadding: EdgeInsets.zero,
          prefixIcon: Icon(
            Icons.search,
            color: Colors.grey[600],
          ),
          enabledBorder: _searchBarOutlineBoder(),
          focusedBorder: _searchBarOutlineBoder(),
          hintText: Translations.of(context).text('search_bar_initial_text'),
        ),
        onChanged: _showSearchResults,
        focusNode: _focusNode,
        controller: _textEditingController,
      ),
    );
  }
}
