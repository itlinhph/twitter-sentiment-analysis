import TwitterAPI

import settings
import twitter


def main():
    api = TwitterAPI.TwitterAPI(** settings.get_app_settings())

    twitter.fetch(api, 'search/tweets', 'infinityWar', {'q': '#metoo'})


if __name__ == '__main__':
    main()
