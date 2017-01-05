import fetch from 'isomorphic-fetch'
import urlJoin from 'url-join'
import qs from 'query-string'

const HOST = ''
const VERSION = ''

const combinePayload = (res: Promise, payload?: { [key: string]: any }) => {
    return Promise.resolve(
        res.json().then((r) => ({
            ...r,
            payload
        }))
    )
}

export default (url: string, options?: { [key: string]: any }={}) => {
    const URL = urlJoin(HOST, VERSION, url)
    let body = {}
    options.credentials = 'includes'
    if (options.method && options.method.toLowerCase() !== 'get') {
        body = options.body || {}
    } else {
        const element = document.createElement('a')
        element.href = URL
        body = qs.parse(element.search)
    }

    return fetch(URL, options).then((res) => {
        if (res.status >= 200 && res.status < 300) {
            return combinePayload(res.json(), body)
        } else {
            return Promise.reject(combinePayload(res.json(), body))
        }
    })
}
