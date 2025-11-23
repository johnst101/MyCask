# Tech Stack and Research

## Chosen Tech Stack

- React (PWA)
- FastAPI
- PostgreSQL

## Research for Each Tech Stack

### Progressive Web App (PWA)

#### [PWA Simple Overview](https://web.dev/articles/pwa-checklist)

##### Core PWA Checklist

- Starts fast, stays fast
  - Speed is critical for users to use your app
  - Use their [guide on fast load times](https://web.dev/explore/fast) to learn how to make the PWA fast and stay fast
- Works in any browser
  - Look at [Resilliant Web Design](https://resilientwebdesign.com/) to learn this well
- Responsive to any screen size
  - Start with mobile first because it requires a focus on the most important features and actions
  - [ ] [Content First Design](https://uxdesign.cc/why-you-should-design-the-content-first-for-better-experiences-374f4ba1fe3c)
  - [ ] [Content Out Responsive Layout](http://alistapart.com/article/content-out-layout/)
  - [ ] [Seven Deadly Mobile Myths](https://www.forbes.com/sites/anthonykosner/2012/05/03/seven-deadly-mobile-myths-josh-clark-debunks-the-desktop-paradigm-and-more/#21ecac977bca)
  - [ ] [PWA Full Tutorial](https://web.dev/learn/pwa)
- Provides a Custom Offline Page
  - Users expect installed apps to work no matter their connection status
  - No blank pages
  - Read [Create an offline fallback page](https://web.dev/articles/offline-fallback-page) to learn how to implement it
- Is Installable
  - Helps with people adopting the app
  - Follow the [installable guide](https://web.dev/articles/customize-install)

##### Optimal PWA Checklist

- Provides an offline experience
  - People want to be able to do certain features offline
  - After determining which features your users expect to work offline, you need to make your content available and adaptable to offline contexts
  - You can use [IndexedDB](https://web.dev/articles/indexeddb), an in-browser NoSQL storage system, to store and retrieve data, and [background sync](https://developer.chrome.com/blog/background-sync/) to let users take actions while offline and defer server communications until the user has a stable connection again
  - You can use service workers to store other kinds of content, such as images, video files, and audio files, for offline use, and to implement [safe, long-lived sessions](https://developer.chrome.com/blog/2-cookie-handoff/) to keep users authenticated
- Fully accessible
  - Must pass the most recent [Web Content Accessibility Guidelines (WCAG) international standard](https://www.w3.org/WAI/standards-guidelines/wcag/)
  - W3C's [Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/) is a good place to start. A majority of accessibility testing must be done manually
  - [Accessibility audit in Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/), [axe](https://github.com/dequelabs/axe-core), and [Accessibility Insights](https://accessibilityinsights.io/) can help you automate some accessibility testing
  - It's also important to use semantically correct elements instead of recreating those elements on your own, such as `<a>` and `<button>` elements. This ensures that when you do need to build more advanced features, accessibility expectations are met, such as when to use arrows versus tabs
- Discoverable in search
  - Start by ensuring that each URL has a unique, descriptive title and meta description. Then you can use the Google Search Console and the Search Engine Optimization audits in Lighthouse to debug and fix discoverability issues with your PWA
  - You can also use Bing's or Yandex's site owner tools, and consider including structured data using schemas from Schema.org in your PWA
- Works with any input type
  - Equally usable with a mouse, keyboard, stylus or touch
  - The [Pointer Events API](https://developer.chrome.com/blog/pointer-events/) provides a unified interface for working with various input options, and is especially good for adding stylus support
- Provides context for permission request
  - The [Permission UX](https://web.dev/articles/push-notifications-permissions-ux) article and UX Planet's [The Right Ways to Ask Users](https://uxplanet.org/mobile-ux-design-the-right-ways-to-ask-users-for-permissions-6cdd9ab25c27) for Permissions are good resources to understand how to design permission prompts that, while focused on mobile, apply to all PWAs
- Follows best practices for healthy code
  - There are a number of high-priority checks to ensure a healthy codebase:
    - Avoid using libraries with known vulnerabilities
    - Make sure you're not using deprecated APIs
    - Remove unsafe coding practices from your codebase, such as `document.write()` or having non-passive scroll event listeners
    - You can even code defensively to make sure your PWA doesn't break if analytics or other third party libraries fail to load
    - Consider requiring static code analysis, like linting, as well as automated testing in multiple browsers and release channels. These techniques can help catch errors before they make it into production

##### Add a web app manifest

A web app manifest is a JSON file that tells the browser how your Progressive Web App (PWA) should behave when installed on the user's desktop or mobile device. At minimum, a typical manifest file includes:

The app's name
The icons the app should use
The URL that should be opened when the app launches

###### Create the manifest file

The manifest file can have any name, but it's commonly named manifest.json and served from the root (your website's top-level directory). The specification suggests the extension should be .webmanifest, but you might want to use JSON files to make your manifests clearer to read

More details [here](https://web.dev/articles/add-manifest)

##### Service Workers

Service workers are JavaScript files that run in the background of a Progressive Web App (PWA) to enable core features like offline access, faster loading, and push notifications. They act as a proxy between the browser and the network, allowing them to intercept and manage network requests, cache resources like HTML, CSS, and images, and perform tasks in the background. A basic service worker has a lifecycle of registration, installation (where assets are cached), and activation (where old caches are cleaned up).

###### How service workers work

- Registration: The process starts by registering the service worker script (e.g., sw.js) with the browser, typically from a main app file.
- Installation: The first event a service worker receives is install. This is the ideal time to cache static assets like HTML, CSS, and JavaScript files for future use.
- Activation: After installation, and once the old version of the service worker is no longer active, the new one receives an activate event. This is used to clean up old caches and update resources.
- Network Request Interception: Once active, the service worker can intercept requests and decide to serve from the cache, fetch from the network, or use another strategy.

###### Important considerations

- HTTPS is required: Because they can intercept requests, service workers require a secure, HTTPS connection to prevent malicious attacks.
- Background process: Service workers run on a separate thread from the main browser thread and have no access to the Document Object Model (DOM).
- Not an automatic feature: Simply having a service worker file doesn't make an app function offline; your code must be written to handle caching and network requests.
- Lifecycle management: You must understand the service worker's lifecycle (registration, installation, and activation) to ensure it works correctly and updates are handled properly.
