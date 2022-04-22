

module.exports = {
    publicPath:
        process.env.NODE_ENV === "production" ? "/datavis-project-2022-mng/" : "/",

    transpileDependencies: [
        'vuetify'
    ]
}
