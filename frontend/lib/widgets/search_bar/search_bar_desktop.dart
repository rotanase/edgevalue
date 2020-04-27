import 'dart:math';

import 'package:flutter/material.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:flappy_search_bar/flappy_search_bar.dart';
import 'package:flappy_search_bar/search_bar_style.dart';
import 'package:flappy_search_bar/scaled_tile.dart';

class Post {
  final String title;
  final String body;

  Post(this.title, this.body);
}

class SearchBarDesktop extends StatefulWidget {
  @override
  _SearchBarDesktopState createState() => _SearchBarDesktopState();
}

class _SearchBarDesktopState extends State<SearchBarDesktop> {
  final SearchBarController<Post> _searchBarController = SearchBarController();

  Future<List<Post>> _getALlPosts(String text) async {
    await Future.delayed(Duration(seconds: text.length == 4 ? 10 : 1));
    if (text.length == 5) throw Error();
    if (text.length == 6) return [];
    List<Post> posts = [];

    var random = new Random();
    for (int i = 0; i < 10; i++) {
      posts.add(Post("$text $i", "body random number : ${random.nextInt(100)}"));
    }
    return posts;
  }

  Widget _onItemFound(Post post, int index) {
    return Container(
      color: Colors.lightBlue,
      child: ListTile(
        title: Text(post.title),
        isThreeLine: true,
        subtitle: Text(post.body),
        onTap: () {
          //Navigator.of(context).push(MaterialPageRoute(builder: (context) => Detail()));
        },
      ),
    );
  }
  
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        width: 500,
        child: SearchBar<Post>(
          searchBarStyle: SearchBarStyle(
            borderRadius: BorderRadius.circular(10),
          ),
          hintText: Translations.of(context).text('search_bar_initial_text'),
          onSearch: _getALlPosts,
          searchBarController: _searchBarController,
          cancellationWidget: Text(Translations.of(context).text('cancel_search_text')),
          emptyWidget: Text(Translations.of(context).text('no_search_result_text')),
          indexedScaledTileBuilder: (int index) => ScaledTile.count(1, index.isEven ? 2 : 1), /// CHECK IT OUT
          onItemFound: _onItemFound,
        ),
      ),
    );
  }
}
