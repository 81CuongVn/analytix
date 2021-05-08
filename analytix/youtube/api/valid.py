from .iso import COUNTRIES, SUBDIVISIONS


CORE_DIMENSIONS = (
    "ageGroup",
    "channel",
    "country",
    "day",
    "gender",
    "month",
    "sharingService",
    "uploaderType",
    "video",
)

CONTENT_OWNER_DIMENSIONS = (
    "claimedStatus",
    "uploaderType",
)

ALL_DIMENSIONS = (
    "video",
    "playlist",
    "channel",
    "country",
    "province",
    "day",
    "month",
    "insightPlaybackLocationType",
    "insightPlaybackLocationDetail",
    "liveOrOnDemand",
    "subscribedStatus",
    "youtubeProduct",
    "insightTrafficSourceType",
    "insightTrafficSourceDetail",
    "deviceType",
    "operatingSystem",
    "ageGroup",
    "gender",
    "sharingService",
    "elapsedVideoTimeRatio",
    "audienceType",
    "adType",
    "claimedStatus",
    "uploaderType",
)

VALID_FILTER_OPTIONS = {
    "video": (),
    "playlist": (),
    "channel": (),
    "group": (),
    "country": COUNTRIES,
    "province": SUBDIVISIONS,
    "continent": (
        "002",
        "019",
        "142",
        "150",
        "009",
    ),
    "subContinent": (
        "014",
        "017",
        "015",
        "018",
        "011",
        "029",
        "013",
        "021",
        "005",
        "143",
        "030",
        "034",
        "035",
        "145",
        "151",
        "154",
        "039",
        "155",
        "053",
        "054",
        "057",
        "061",
    ),
    "day": (),
    "month": (),
    "insightPlaybackLocationType": (
        "BROWSE",
        "CHANNEL",
        "EMBEDDED",
        "EXTERNAL_APP",
        "MOBILE",
        "SEARCH",
        "WATCH",
        "YT_OTHER",
    ),
    "insightPlaybackLocationDetail": (),
    "liveOrOnDemand": (
        "LIVE",
        "ON_DEMAND",
    ),
    "subscribedStatus": (
        "SUBSCRIBED",
        "UNSUBSCRIBED",
    ),
    "youtubeProduct": (
        "CORE",
        "GAMING",
        "KIDS",
        "UNKNOWN",
    ),
    "insightTrafficSourceType": (
        "ADVERTISING",
        "ANNOTATION",
        "CAMPAIGN_CARD",
        "END_SCREEN",
        "EXT_URL",
        "NO_LINK_EMBEDDED",
        "NO_LINK_OTHER",
        "NOTIFICATION",
        "PLAYLIST",
        "PROMOTED",
        "RELATED_VIDEO",
        "SHORTS",
        "SUBSCRIBER",
        "YT_CHANNEL",
        "YT_OTHER_PAGE",
        "YT_PLAYLIST_PAGE",
        "YT_SEARCH",
    ),
    "insightTrafficSourceDetail": (
        "ADVERTISING",
        "CAMPAIGN_CARD",
        "END_SCREEN",
        "EXT_URL",
        "NOTIFICATION",
        "RELATED_VIDEO",
        "SUBSCRIBER",
        "YT_CHANNEL",
        "YT_OTHER_PAGE",
        "YT_SEARCH",
    ),
    "deviceType": (
        "DESKTOP",
        "GAME_CONSOLE",
        "MOBILE",
        "TABLET",
        "TV",
        "UNKNOWN_PLATFORM",
    ),
    "operatingSystem": (
        "ANDROID",
        "BADA",
        "BLACKBERRY",
        "CHROMECAST",
        "DOCOMO",
        "FIREFOX",
        "HIPTOP",
        "IOS",
        "KAIOS",
        "LINUX",
        "MACINTOSH",
        "MEEGO",
        "NINTENDO_3DS",
        "OTHER",
        "PLAYSTATION",
        "PLAYSTATION_VITA",
        "REALMEDIA",
        "SMART_TV",
        "SYMBIAN",
        "TIZEN",
        "WEBOS",
        "WII",
        "WINDOWS",
        "WINDOWS_MOBILE",
        "XBOX",
    ),
    "ageGroup": (
        "age13-17",
        "age18-24",
        "age25-34",
        "age35-44",
        "age45-54",
        "age55-64",
        "age65-",
    ),
    "gender": (
        "female",
        "male",
    ),
    "sharingService": (
        "AMEBA",
        "ANDROID_EMAIL",
        "ANDROID_MESSENGER",
        "ANDROID_MMS",
        "BBM",
        "BLOGGER",
        "COPY_PASTE",
        "CYWORLD",
        "DIGG",
        "DROPBOX",
        "EMBED",
        "MAIL",
        "FACEBOOK",
        "FACEBOOK_MESSENGER",
        "FACEBOOK_PAGES",
        "FOTKA",
        "GMAIL",
        "GOO",
        "GOOGLEPLUS",
        "GO_SMS",
        "GROUPME",
        "HANGOUTS",
        "HI5",
        "HTC_MMS",
        "INBOX",
        "IOS_SYSTEM_ACTIVITY_DIALOG",
        "KAKAO_STORY",
        "KAKAO",
        "KIK",
        "LGE_EMAIL",
        "LINE",
        "LINKEDIN",
        "LIVEJOURNAL",
        "MENEAME",
        "MIXI",
        "MOTOROLA_MESSAGING",
        "MYSPACE",
        "NAVER",
        "NEARBY_SHARE",
        "NUJIJ",
        "ODNOKLASSNIKI",
        "OTHER",
        "PINTEREST",
        "RAKUTEN",
        "REDDIT",
        "SKYPE",
        "SKYBLOG",
        "SONY_CONVERSATIONS",
        "STUMBLEUPON",
        "TELEGRAM",
        "TEXT_MESSAGE",
        "TUENTI",
        "TUMBLR",
        "TWITTER",
        "UNKNOWN",
        "VERIZON_MMS",
        "VIBER",
        "VKONTATKE",
        "WECHAT",
        "WEIBO",
        "WHATS_APP",
        "WYKOP",
        "YAHOO",
        "YOUTUBE_GAMING",
        "YOUTUBE_KIDS",
        "YOUTUBE_MUSIC",
        "YOUTUBE_TV",
    ),
    "elapsedVideoTimeRatio": tuple(f"{n/100}" for n in range(1, 101)),
    "audienceType": (
        "ORGANIC",
        "AD_INSTREAM",
        "AD_INDISPLAY",
    ),
    "adType": (
        "auctionBumperInstream",
        "auctionDisplay",
        "auctionInstream",
        "auctionTrueviewInslate",
        "auctionTrueviewInstream",
        "auctionUnknown",
        "reservedBumperInstream",
        "reservedClickToPlay",
        "reservedDisplay",
        "reservedInstream",
        "reservedInstreamSelect",
        "reservedMasthead",
        "reservedUnknown",
        "unknown",
    ),
    "claimedStatus": ("claimed",),
    "uploaderType": (
        "self",
        "thirdParty",
    ),
}

ALL_FILTERS = tuple(VALID_FILTER_OPTIONS.keys())

CORE_METRICS = (
    "annotationClickThroughRate",
    "annotationCloseRate",
    "averageViewDuration",
    "comments",
    "dislikes",
    "estimatedMinutesWatched",
    "estimatedRevenue",
    "likes",
    "shares",
    "subscribersGained",
    "subscribersLost",
    "viewerPercentage",
    "views",
)

ALL_METRICS = (
    "views",
    "redViews",
    "comments",
    "likes",
    "dislikes",
    "videosAddedToPlaylists",
    "videosRemovedFromPlaylists",
    "shares",
    "estimatedMinutesWatched",
    "estimatedRedMinutesWatched",
    "averageViewDuration",
    "averageViewPercentage",
    "annotationClickThroughRate",
    "annotationCloseRate",
    "annotationImpressions",
    "annotationClickableImpressions",
    "annotationClosableImpressions",
    "annotationClicks",
    "annotationCloses",
    "cardClickRate",
    "cardTeaserClickRate",
    "cardImpressions",
    "cardTeaserImpressions",
    "cardClicks",
    "cardTeaserClicks",
    "subscribersGained",
    "subscribersLost",
    "estimatedRevenue",
    "estimatedAdRevenue",
    "grossRevenue",
    "estimatedRedPartnerRevenue",
    "monetizedPlaybacks",
    "playbackBasedCpm",
    "adImpressions",
    "cpm",
)

ALL_PROVINCE_METRICS = (
    "views",
    "redViews",
    "estimatedMinutesWatched",
    "estimatedRedMinutesWatched",
    "averageViewDuration",
    "averageViewPercentage",
    "annotationClickThroughRate",
    "annotationCloseRate",
    "annotationImpressions",
    "annotationClickableImpressions",
    "annotationClosableImpressions",
    "annotationClicks",
    "annotationCloses",
    "cardClickRate",
    "cardTeaserClickRate",
    "cardImpressions",
    "cardTeaserImpressions",
    "cardClicks",
    "cardTeaserClicks",
)

SUBSCRIPTION_METRICS = (
    "views",
    "redViews",
    "likes",
    "dislikes",
    "videosAddedToPlaylists",
    "videosRemovedFromPlaylists",
    "shares",
    "estimatedMinutesWatched",
    "estimatedRedMinutesWatched",
    "averageViewDuration",
    "averageViewPercentage",
    "annotationClickThroughRate",
    "annotationCloseRate",
    "annotationImpressions",
    "annotationClickableImpressions",
    "annotationClosableImpressions",
    "annotationClicks",
    "annotationCloses",
    "cardClickRate",
    "cardTeaserClickRate",
    "cardImpressions",
    "cardTeaserImpressions",
    "cardClicks",
    "cardTeaserClicks",
)

LIVE_PLAYBACK_DETAIL_METRICS = (
    "views",
    "redViews",
    "estimatedMinutesWatched",
    "estimatedRedMinutesWatched",
    "averageViewDuration",
)

VIEW_PERCENTAGE_PLAYBACK_DETAIL_METRICS = (
    "views",
    "redViews",
    "estimatedMinutesWatched",
    "estimatedRedMinutesWatched",
    "averageViewDuration",
    "averageViewPercentage",
)

LOCATION_AND_TRAFFIC_METRICS = (
    "views",
    "estimatedMinutesWatched",
)

ALL_PLAYLIST_METRICS = (
    "views",
    "redViews",
    "estimatedMinutesWatched",
    "estimatedRedMinutesWatched",
    "averageViewDuration",
    "playlistStarts",
    "viewsPerPlaylistStart",
    "averageTimeInPlaylist",
)

LOCATION_AND_TRAFFIC_PLAYLIST_METRICS = (
    "views",
    "estimatedMinutesWatched",
    "playlistStarts",
    "viewsPerPlaylistStart",
    "averageTimeInPlaylist",
)
