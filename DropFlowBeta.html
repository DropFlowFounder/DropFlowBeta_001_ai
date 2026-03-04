<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DropFlow 2.0 - Telegram Mini App</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
        
        :root {
            --tg-theme-bg-color: #0f172a;
            --tg-theme-text-color: #f8fafc;
            --tg-theme-hint-color: #94a3b8;
            --tg-theme-link-color: #60a5fa;
            --tg-theme-button-color: #4f46e5;
            --tg-theme-button-text-color: #ffffff;
        }
        
        body {
            font-family: 'Inter', 'Space Grotesk', sans-serif;
            background-color: var(--tg-theme-bg-color);
            color: var(--tg-theme-text-color);
            overscroll-behavior: none;
            -webkit-tap-highlight-color: transparent;
            padding-bottom: 5rem;
        }
        
        /* Improved dark mode experience */
        .dark-section {
            background-color: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .nft-card {
            background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
            border: 1px solid rgba(79, 70, 229, 0.3);
            box-shadow: 0 4px 20px rgba(79, 70, 229, 0.1);
        }
        
        .crypto-gradient {
            background: linear-gradient(135deg, #4f46e5 0%, #8b5cf6 50%, #ec4899 100%);
        }
        
        .crypto-glow {
            box-shadow: 0 0 20px rgba(79, 70, 229, 0.5);
        }
        
        .gradient-text {
            background: linear-gradient(90deg, #4f46e5, #8b5cf6, #ec4899);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        /* Enhanced animations */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        
        .float {
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .pulse {
            animation: pulse 1.5s infinite;
        }
        
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        .cart-item-animation {
            animation: slideIn 0.3s ease-out forwards;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(30, 41, 59, 0.5);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #4f46e5, #8b5cf6);
            border-radius: 10px;
        }
        
        /* Grid patterns */
        .grid-pattern {
            background: 
                linear-gradient(rgba(30, 41, 59, 0.8) 1px, transparent 1px),
                linear-gradient(90deg, rgba(30, 41, 59, 0.8) 1px, transparent 1px);
            background-size: 20px 20px;
        }
        
        .nft-border {
            border: 2px solid transparent;
            border-image: linear-gradient(45deg, #8b5cf6, #ec4899, #f97316) 1;
        }
        
        .status-processing { background: linear-gradient(90deg, #4f46e5, #8b5cf6); }
        .status-shipped { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
        .status-delivered { background: linear-gradient(90deg, #10b981, #34d399); }
        .status-canceled { background: linear-gradient(90deg, #ef4444, #f87171); }
        
        .ton-pattern {
            background: 
                radial-gradient(circle at 10% 20%, rgba(45, 156, 219, 0.1) 0%, transparent 20%),
                radial-gradient(circle at 80% 80%, rgba(45, 156, 219, 0.1) 0%, transparent 20%);
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        
        .qr-code {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border: 1px solid rgba(79, 70, 229, 0.3);
        }
        
        .crypto-chart-container {
            height: 180px;
        }
        
        .wallet-shimmer {
            position: relative;
            overflow: hidden;
        }
        
        .wallet-shimmer::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(255, 255, 255, 0.1) 50%, 
                transparent 100%);
            animation: shimmer 1.5s infinite;
        }
        
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        .profile-banner {
            background: linear-gradient(135deg, #4f46e5 0%, #8b5cf6 50%, #ec4899 100%);
            min-height: 120px;
            position: relative;
        }
    </style>
</head>
<body class="bg-gray-900 text-white antialiased">
    <!-- App container -->
    <div id="app" class="min-h-screen max-w-md mx-auto relative overflow-x-hidden pb-16"></div>
    
    <!-- Modals (keep existing modals here) -->
    <div id="store-creation-modal" class="fixed inset-0 bg-black bg-opacity-75 z-50 hidden items-center justify-center p-4">
        <!-- Keep existing store creation modal code -->
    </div>
    
    <div id="crypto-payment-modal" class="fixed inset-0 bg-black bg-opacity-75 z-50 hidden items-center justify-center p-4">
        <!-- Keep existing crypto payment modal code -->
    </div>
    
    <div id="nft-modal" class="fixed inset-0 bg-black bg-opacity-75 z-50 hidden items-center justify-center p-4">
        <!-- Keep existing NFT modal code -->
    </div>
    
    <div id="quests-modal" class="fixed inset-0 bg-black bg-opacity-75 z-50 hidden items-center justify-center p-4">
        <!-- Keep existing quests modal code -->
    </div>

    <script>
        // Expand Telegram WebApp to full view
        const tg = window.Telegram.WebApp;
        tg.expand();
        
        // Apply Telegram theme variables if available
        if (tg.themeParams) {
            document.documentElement.style.setProperty('--tg-theme-bg-color', tg.themeParams.bg_color || '#0f172a');
            document.documentElement.style.setProperty('--tg-theme-text-color', tg.themeParams.text_color || '#f8fafc');
            document.documentElement.style.setProperty('--tg-theme-hint-color', tg.themeParams.hint_color || '#94a3b8');
            document.documentElement.style.setProperty('--tg-theme-link-color', tg.themeParams.link_color || '#60a5fa');
            document.documentElement.style.setProperty('--tg-theme-button-color', tg.themeParams.button_color || '#4f46e5');
            document.documentElement.style.setProperty('--tg-theme-button-text-color', tg.themeParams.button_text_color || '#ffffff');
        }
        
        // Enhanced state for the entire application
        let appState = {
            currentPage: 'dashboard',
            user: {
                id: tg.initDataUnsafe.user?.id || '12345',
                name: tg.initDataUnsafe.user?.first_name || 'Alex',
                balance: 15423,
                cryptoBalance: 287.34,
                username: tg.initDataUnsafe.user?.username || 'dropflow_user',
                isVerified: true,
                stores: [],
                activity: []
            },
            notifications: [],
            products: [],
            categories: ["All", "Fashion", "Electronics", "Home", "Sports", "Beauty"],
            selectedCategory: "All",
            cart: [],
            orders: [],
            stores: [],
            currentStore: null,
            quests: [
                { id: 1, title: "Complete First Purchase", reward: 25, completed: true },
                { id: 2, title: "Invite a Friend", reward: 100, completed: false },
                { id: 3, title: "Write a Review", reward: 15, completed: false },
                { id: 4, title: "Share on Stories", reward: 50, completed: false },
                { id: 5, title: "Create Your Store", reward: 150, completed: false }
            ],
            nfts: [
                {
                    id: 1,
                    title: "First Purchase",
                    image: "https://picsum.photos/400/400?random=1",
                    reward: "25 DRP",
                    date: "2023-05-15",
                    collection: "Dropshipper Starter"
                },
                {
                    id: 2,
                    title: "Gold Shopper",
                    image: "https://picsum.photos/400/400?random=2",
                    reward: "50 DRP",
                    date: "2023-06-22",
                    collection: "Loyal Customers"
                },
                {
                    id: 3,
                    title: "Crypto Pioneer",
                    image: "https://picsum.photos/400/400?random=3",
                    reward: "100 DRP",
                    date: "2023-07-01",
                    collection: "Crypto Payments"
                }
            ],
            cryptoPrices: {
                DRP: 1.25,
                BTC: 30350.42,
                ETH: 1903.67,
                TON: 1.85,
                USDT: 1.00,
                BNB: 241.58
            },
            cryptoAssets: [
                { symbol: "TON", balance: 5.75, change: 4.3 },
                { symbol: "BTC", balance: 0.0021, change: -1.2 },
                { symbol: "ETH", balance: 0.082, change: 3.1 },
                { symbol: "BNB", balance: 2.5, change: 2.7 },
                { symbol: "USDT", balance: 1250, change: 0 }
            ],
            transactions: [
                { id: 1, type: "receive", crypto: "TON", amount: 1.2, date: "2023-07-22", status: "completed" },
                { id: 2, type: "send", crypto: "DRP", amount: 58.4, date: "2023-07-20", status: "completed" },
                { id: 3, type: "swap", crypto: "ETH", amount: 0.032, date: "2023-07-18", status: "completed" },
                { id: 4, type: "buy", crypto: "BNB", amount: 1.5, date: "2023-07-15", status: "completed" },
                { id: 5, type: "receive", crypto: "TON", amount: 0.85, date: "2023-07-12", status: "completed" }
            ],
            profileStats: {
                nftsCollected: 8,
                questsCompleted: 12,
                storesOwned: 3,
                daysActive: 64
            }
        };
        
        // Initialize sample data
        function initializeSampleData() {
            // Sample products
            appState.products = [
                {
                    id: 1,
                    name: "Nike Air Max 270",
                    price: 11200,
                    cryptoPrice: 89.60,
                    image: "https://picsum.photos/300/300?random=10",
                    category: "Fashion",
                    description: "The Nike Air Max 270 React fuses iconic Air Max DNA with a sleek, modern design. Featuring the largest heel Air unit to date, it delivers incredible comfort all day long.",
                    stock: 25,
                    rating: 4.8,
                    store: "UrbanKicks"
                },
                {
                    id: 2,
                    name: "iPhone 14 Pro Case",
                    price: 2499,
                    cryptoPrice: 19.99,
                    image: "https://picsum.photos/300/300?random=11",
                    category: "Electronics",
                    description: "Premium protective case for iPhone 14 Pro. Features shock absorption and raised edges to protect your screen and camera.",
                    stock: 50,
                    rating: 4.5,
                    store: "TechGuard"
                },
                {
                    id: 3,
                    name: "Smart Fitness Watch",
                    price: 8999,
                    cryptoPrice: 71.99,
                    image: "https://picsum.photos/300/300?random=12",
                    category: "Electronics",
                    description: "Track your heart rate, steps, sleep patterns and more. Water-resistant with 10-day battery life. Syncs with all major smartphones.",
                    stock: 12,
                    rating: 4.7,
                    store: "FitGadgets"
                },
                {
                    id: 4,
                    name: "Wireless Headphones",
                    price: 5999,
                    cryptoPrice: 47.99,
                    image: "https://picsum.photos/300/300?random=13",
                    category: "Electronics",
                    description: "Premium noise-cancelling headphones with 30-hour battery life. Features touch controls and voice assistant support.",
                    stock: 18,
                    rating: 4.6,
                    store: "SoundSphere"
                },
                {
                    id: 5,
                    name: "Designer Sunglasses",
                    price: 4599,
                    cryptoPrice: 36.79,
                    image: "https://picsum.photos/300/300?random=14",
                    category: "Fashion",
                    description: "UV-protection sunglasses with polarized lenses. Sleek metal frame with comfortable nose pads for all-day wear.",
                    stock: 30,
                    rating: 4.9,
                    store: "StyleMasters"
                },
                {
                    id: 6,
                    name: "Premium Yoga Mat",
                    price: 2999,
                    cryptoPrice: 23.99,
                    image: "https://picsum.photos/300/300?random=15",
                    category: "Sports",
                    description: "Eco-friendly, non-slip yoga mat with alignment markers. Extra thick for joint protection and comfortable poses.",
                    stock: 40,
                    rating: 4.7,
                    store: "ZenLife"
                }
            ];
            
            // Sample stores
            appState.stores = [
                {
                    id: 1,
                    name: "UrbanKicks",
                    category: "Fashion",
                    owner: appState.user.id,
                    products: [1],
                    rating: 4.8,
                    sales: 42,
                    color: "#6366f1",
                    created: "2023-05-10"
                },
                {
                    id: 2,
                    name: "TechGuard",
                    category: "Electronics",
                    owner: appState.user.id,
                    products: [2],
                    rating: 4.5,
                    sales: 87,
                    color: "#3b82f6",
                    created: "2023-04-22"
                },
                {
                    id: 3,
                    name: "ZenLife",
                    category: "Sports",
                    owner: "user123",
                    products: [6],
                    rating: 4.7,
                    sales: 156,
                    color: "#10b981",
                    created: "2023-03-15"
                }
            ];
            
            // Sample orders
            appState.orders = [
                {
                    id: "#DRP-2381",
                    date: "2023-07-15",
                    status: "delivered",
                    items: [
                        { productId: 1, quantity: 1, price: 11200 },
                        { productId: 2, quantity: 2, price: 2499 }
                    ],
                    total: 16198,
                    cryptoTotal: 129.58,
                    paymentMethod: "DRP",
                    tracking: "DHL-8G438H293J",
                    nftId: 1
                },
                {
                    id: "#DRP-2210",
                    date: "2023-07-10",
                    status: "shipped",
                    items: [
                        { productId: 3, quantity: 1, price: 8999 }
                    ],
                    total: 8999,
                    cryptoTotal: 71.99,
                    paymentMethod: "TON",
                    tracking: "UPS-1ZA38F291Y",
                    nftId: null
                },
                {
                    id: "#DRP-2157",
                    date: "2023-06-28",
                    status: "processing",
                    items: [
                        { productId: 4, quantity: 1, price: 5999 },
                        { productId: 6, quantity: 1, price: 2999 }
                    ],
                    total: 8998,
                    cryptoTotal: 71.98,
                    paymentMethod: "BTC",
                    tracking: null,
                    nftId: null
                }
            ];
            
            // Set user store information
            appState.user.stores = [1, 2];
            
            // User activity data
            appState.user.activity = [
                { id: 1, type: "store_created", name: "TechGuard", date: "2023-07-10", icon: "store" },
                { id: 2, type: "nft_received", name: "Crypto Pioneer", date: "2023-07-05", icon: "award" },
                { id: 3, type: "store_created", name: "UrbanKicks", date: "2023-06-22", icon: "store" },
                { id: 4, type: "quest_completed", name: "Crypto Pioneer", date: "2023-06-18", icon: "trophy" },
                { id: 5, type: "first_login", name: "Welcome to DropFlow", date: "2023-06-10", icon: "user-plus" }
            ];
        }
        
        // Calculate cart totals
        function getCartTotal() {
            return appState.cart.reduce((total, item) => {
                return total + (item.product.price * item.quantity);
            }, 0);
        }
        
        function getCryptoCartTotal() {
            return appState.cart.reduce((total, item) => {
                return total + (item.product.cryptoPrice * item.quantity);
            }, 0);
        }
        
        function getCartItemCount() {
            return appState.cart.reduce((count, item) => count + item.quantity, 0);
        }
        
        // Navigation system
        function navigate(page) {
            appState.currentPage = page;
            renderApp();
        }
        
        // Render navigation bar
        function renderNavBar(activePage) {
            return `
                <nav class="fixed bottom-0 left-0 right-0 bg-gray-900 border-t border-gray-800 flex justify-around py-3">
                    <button data-navigate="dashboard" class="flex flex-col items-center ${activePage === 'dashboard' ? 'text-indigo-400' : 'text-gray-400'}">
                        <i class="fas fa-home text-xl"></i>
                        <span class="text-xs mt-1">Home</span>
                    </button>
                    <button data-navigate="market" class="flex flex-col items-center ${activePage === 'market' ? 'text-indigo-400' : 'text-gray-400'}">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="text-xs mt-1">Market</span>
                    </button>
                    <button data-action="open-create-store-modal" class="flex flex-col items-center text-gray-400 relative">
                        <div class="w-12 h-12 rounded-full gradient-bg flex items-center justify-center -mt-6 crypto-glow">
                            <i class="fas fa-plus text-white"></i>
                        </div>
                        <span class="text-xs mt-1">Create</span>
                    </button>
                    <button data-navigate="wallet" class="flex flex-col items-center ${activePage === 'wallet' ? 'text-indigo-400' : 'text-gray-400'}">
                        <i class="fas fa-wallet text-xl"></i>
                        <span class="text-xs mt-1">Wallet</span>
                    </button>
                    <button data-navigate="profile" class="flex flex-col items-center ${activePage === 'profile' ? 'text-indigo-400' : 'text-gray-400'}">
                        <i class="fas fa-user-circle text-xl"></i>
                        <span class="text-xs mt-1">Profile</span>
                    </button>
                </nav>
            `;
        }
        
        // Wallet screen
        function renderWallet() {
            const totalBalance = appState.cryptoAssets.reduce((sum, asset) => {
                const price = appState.cryptoPrices[asset.symbol] || 0;
                return sum + (asset.balance * price);
            }, appState.user.cryptoBalance * appState.cryptoPrices.DRP);
            
            return `
                <div>
                    <header class="sticky top-0 z-10 bg-gray-900 border-b border-gray-800 px-4 py-3">
                        <div class="flex justify-between items-center">
                            <button data-navigate="dashboard">
                                <i class="fas fa-arrow-left text-xl"></i>
                            </button>
                            <h1 class="text-xl font-bold">Crypto Wallet</h1>
                            <button data-action="open-quests">
                                <i class="fas fa-trophy text-xl"></i>
                            </button>
                        </div>
                    </header>
                    
                    <main class="p-4 pb-24">
                        <div class="bg-gradient-to-r from-indigo-900 to-purple-900 rounded-2xl p-5 mb-6 text-center">
                            <p class="text-gray-300 text-sm mb-1">Total Balance</p>
                            <p class="text-3xl font-bold mb-1">$${totalBalance.toFixed(2)}</p>
                            <p class="text-indigo-200 text-sm">≈ ${appState.user.cryptoBalance.toFixed(2)} DRP</p>
                            
                            <div class="flex justify-center gap-4 mt-5">
                                <button class="bg-white/10 hover:bg-white/20 rounded-lg py-3 px-5 flex items-center justify-center">
                                    <i class="fas fa-exchange-alt mr-2"></i> Swap
                                </button>
                                <button class="bg-indigo-600 hover:bg-indigo-700 rounded-lg py-3 px-5 flex items-center justify-center">
                                    <i class="fas fa-plus mr-2"></i> Buy
                                </button>
                            </div>
                        </div>
                        
                        <div class="mb-6">
                            <div class="flex justify-between items-center mb-3">
                                <h2 class="font-bold text-lg">Your Assets</h2>
                                <button class="text-indigo-400 text-sm">View All</button>
                            </div>
                            
                            <div class="space-y-3">
                                <div class="bg-gray-800/50 rounded-xl p-4 flex items-center">
                                    <div class="w-12 h-12 rounded-full bg-indigo-600 flex items-center justify-center mr-3">
                                        <i class="fas fa-coins text-white text-xl"></i>
                                    </div>
                                    <div class="flex-1">
                                        <p class="font-medium">DropCoin (DRP)</p>
                                        <p class="text-xs text-gray-400">${appState.user.cryptoBalance.toFixed(2)} DRP</p>
                                    </div>
                                    <div class="text-right">
                                        <p class="font-bold">$${(appState.user.cryptoBalance * appState.cryptoPrices.DRP).toFixed(2)}</p>
                                        <p class="text-xs text-green-400">+2.8%</p>
                                    </div>
                                </div>
                                
                                ${appState.cryptoAssets.map(asset => {
                                    const changeColor = asset.change >= 0 ? 'text-green-400' : 'text-red-400';
                                    const changeIcon = asset.change >= 0 ? 'arrow-up' : 'arrow-down';
                                    return `
                                        <div class="bg-gray-800/50 rounded-xl p-4 flex items-center">
                                            <div class="w-12 h-12 rounded-full ${asset.symbol === 'TON' ? 'bg-blue-600' : asset.symbol === 'BTC' ? 'bg-yellow-600' : asset.symbol === 'ETH' ? 'bg-purple-600' : asset.symbol === 'BNB' ? 'bg-yellow-500' : 'bg-green-600'} flex items-center justify-center mr-3">
                                                ${
                                                    asset.symbol === 'TON' ? '<i class="fab fa-telegram text-white"></i>' :
                                                    asset.symbol === 'BTC' ? '<i class="fab fa-bitcoin text-white"></i>' :
                                                    asset.symbol === 'ETH' ? '<i class="fab fa-ethereum text-white"></i>' :
                                                    asset.symbol === 'BNB' ? '<span class="font-bold text-white">B</span>' :
                                                    '<i class="fas fa-dollar-sign text-white"></i>'
                                                }
                                            </div>
                                            <div class="flex-1">
                                                <p class="font-medium">${asset.symbol}</p>
                                                <p class="text-xs text-gray-400">${asset.balance.toFixed(4)} ${asset.symbol}</p>
                                            </div>
                                            <div class="text-right">
                                                <p class="font-bold">$${(asset.balance * appState.cryptoPrices[asset.symbol]).toFixed(2)}</p>
                                                <p class="text-xs ${changeColor}">${asset.change > 0 ? '+' : ''}${asset.change.toFixed(1)}% <i class="fas fa-${changeIcon} text-xs"></i></p>
                                            </div>
                                        </div>
                                    `;
                                }).join('')}
                            </div>
                        </div>
                        
                        <div>
                            <div class="flex justify-between items-center mb-3">
                                <h2 class="font-bold text-lg">Recent Transactions</h2>
                                <button class="text-indigo-400 text-sm">View All</button>
                            </div>
                            
                            <div class="space-y-3">
                                ${appState.transactions.map(tx => {
                                    const typeColors = {
                                        receive: 'bg-green-900/30 text-green-400',
                                        send: 'bg-purple-900/30 text-purple-400',
                                        swap: 'bg-indigo-900/30 text-indigo-400',
                                        buy: 'bg-yellow-900/30 text-yellow-400'
                                    };
                                    
                                    const typeIcons = {
                                        receive: 'arrow-down',
                                        send: 'arrow-up',
                                        swap: 'exchange-alt',
                                        buy: 'cart-plus'
                                    };
                                    
                                    return `
                                        <div class="bg-gray-800/50 rounded-xl p-4 flex items-center">
                                            <div class="w-10 h-10 rounded-full ${typeColors[tx.type]} flex items-center justify-center mr-3">
                                                <i class="fas fa-${typeIcons[tx.type]}"></i>
                                            </div>
                                            <div class="flex-1">
                                                <p class="font-medium capitalize">${tx.type}</p>
                                                <p class="text-xs text-gray-400">${tx.date}</p>
                                            </div>
                                            <div class="text-right">
                                                <p class="font-medium ${tx.type === 'receive' || tx.type === 'buy' ? 'text-green-400' : 'text-gray-300'}">
                                                    ${tx.type === 'receive' || tx.type === 'buy' ? '+' : '-'}${tx.amount.toFixed(2)} ${tx.crypto}
                                                </p>
                                            </div>
                                        </div>
                                    `;
                                }).join('')}
                            </div>
                        </div>
                    </main>
                    
                    ${renderNavBar('wallet')}
                </div>
            `;
        }
        
        // Profile screen
        function renderProfile() {
            return `
                <div>
                    <div class="profile-banner rounded-b-3xl overflow-hidden">
                        <div class="absolute inset-0 bg-black/30"></div>
                        <div class="relative p-5 pt-8">
                            <div class="flex justify-between">
                                <button data-navigate="dashboard">
                                    <i class="fas fa-arrow-left text-xl"></i>
                                </button>
                                <button data-action="open-settings">
                                    <i class="fas fa-cog text-xl"></i>
                                </button>
                            </div>
                            <div class="flex items-center mt-4">
                                <img src="https://picsum.photos/100/100?random=avatar" alt="User Avatar" class="w-20 h-20 rounded-full border-4 border-white">
                                <div class="ml-4">
                                    <div class="flex items-center">
                                        <h1 class="text-xl font-bold">${appState.user.name}</h1>
                                        ${appState.user.isVerified ? '<span class="ml-2 text-blue-400"><i class="fas fa-badge-check"></i></span>' : ''}
                                    </div>
                                    <p class="text-gray-200 text-sm">@${appState.user.username}</p>
                                    <button class="bg-white/10 text-xs px-3 py-1 rounded-full mt-2 hover:bg-white/20">
                                        <i class="fas fa-pen mr-1"></i> Edit Profile
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <main class="p-4 pb-24">
                        <div class="grid grid-cols-4 gap-3 mb-6">
                            <div class="bg-gray-800/50 rounded-xl p-3 text-center">
                                <p class="font-bold text-xl">${appState.profileStats.daysActive}</p>
                                <p class="text-xs text-gray-400">Days</p>
                            </div>
                            <div class="bg-gray-800/50 rounded-xl p-3 text-center">
                                <p class="font-bold text-xl">${appState.profileStats.nftsCollected}</p>
                                <p class="text-xs text-gray-400">NFTs</p>
                            </div>
                            <div class="bg-gray-800/50 rounded-xl p-3 text-center">
                                <p class="font-bold text-xl">${appState.profileStats.questsCompleted}</p>
                                <p class="text-xs text-gray-400">Quests</p>
                            </div>
                            <div class="bg-gray-800/50 rounded-xl p-3 text-center">
                                <p class="font-bold text-xl">${appState.profileStats.storesOwned}</p>
                                <p class="text-xs text-gray-400">Stores</p>
                            </div>
                        </div>
                        
                        <div class="bg-gray-800/50 rounded-xl p-4 mb-6">
                            <h2 class="font-bold mb-3">Balance & Rewards</h2>
                            <div class="grid grid-cols-2 gap-3">
                                <div class="bg-indigo-900/30 rounded-xl p-3">
                                    <p class="text-gray-300 text-xs">DropCoin Balance</p>
                                    <p class="font-bold text-lg">${appState.user.cryptoBalance.toFixed(2)} DRP</p>
                                    <p class="text-gray-400 text-xs">≈ $${(appState.user.cryptoBalance * appState.cryptoPrices.DRP).toFixed(2)}</p>
                                </div>
                                <div class="bg-purple-900/30 rounded-xl p-3">
                                    <p class="text-gray-300 text-xs">Active Rewards</p>
                                    <p class="font-bold text-lg">150 DRP</p>
                                    <p class="text-gray-400 text-xs">Complete quests to earn</p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="mb-6">
                            <div class="flex justify-between items-center mb-3">
                                <h2 class="font-bold">Recent Activity</h2>
                                <button class="text-indigo-400 text-sm">View All</button>
                            </div>
                            
                            <div class="space-y-3">
                                ${appState.user.activity.map(item => {
                                    const colors = {
                                        store_created: 'text-blue-400',
                                        nft_received: 'text-purple-400',
                                        quest_completed: 'text-yellow-400',
                                        first_login: 'text-indigo-400'
                                    };
                                    
                                    const icons = {
                                        store_created: 'store',
                                        nft_received: 'award',
                                        quest_completed: 'trophy',
                                        first_login: 'user-plus'
                                    };
                                    
                                    return `
                                        <div class="bg-gray-800/50 rounded-xl p-4 flex items-center">
                                            <div class="w-10 h-10 rounded-full bg-gray-700 flex items-center justify-center mr-3 ${colors[item.type]}">
                                                <i class="fas fa-${icons[item.type]}"></i>
                                            </div>
                                            <div class="flex-1">
                                                <p class="font-medium">${item.name}</p>
                                                <p class="text-xs text-gray-400 capitalize">${item.type.replace('_', ' ')} · ${item.date}</p>
                                            </div>
                                        </div>
                                    `;
                                }).join('')}
                            </div>
                        </div>
                        
                        <div>
                            <h2 class="font-bold mb-3">Your NFTs</h2>
                            <div class="flex space-x-4 overflow-x-auto pb-2 scrollbar-hide">
                                ${appState.nfts.map(nft => `
                                    <div class="nft-card flex-shrink-0 w-36 rounded-2xl overflow-hidden">
                                        <div class="relative">
                                            <img src="${nft.image}" alt="${nft.title}" class="w-full h-32 object-cover">
                                            <div class="absolute top-2 right-2 bg-indigo-600 text-white text-xs px-2 py-1 rounded-full">
                                                NFT
                                            </div>
                                        </div>
                                        <div class="p-2">
                                            <h3 class="font-bold text-sm truncate">${nft.title}</h3>
                                            <p class="text-xs text-gray-400">${nft.collection}</p>
                                            <div class="flex items-center justify-between mt-1">
                                                <span class="text-xs text-amber-400">${nft.reward}</span>
                                                <span class="text-xs text-gray-500">${nft.date}</span>
                                            </div>
                                        </div>
                                    </div>
                                `).join('')}
                                <button class="flex-shrink-0 w-36 rounded-2xl bg-gray-800/50 flex flex-col items-center justify-center">
                                    <div class="w-10 h-10 rounded-full bg-indigo-600 flex items-center justify-center mb-2">
                                        <i class="fas fa-plus text-white"></i>
                                    </div>
                                    <p class="text-sm font-medium">View More</p>
                                </button>
                            </div>
                        </div>
                    </main>
                    
                    ${renderNavBar('profile')}
                </div>
            `;
        }
        
        // Main rendering function
        function renderApp() {
            const appEl = document.getElementById('app');
            
            switch(appState.currentPage) {
                case 'dashboard':
                    appEl.innerHTML = renderDashboard();
                    break;
                case 'market':
                    appEl.innerHTML = renderMarketplace();
                    break;
                case 'store':
                    appEl.innerHTML = renderStoreManagement();
                    break;
                case 'product':
                    appEl.innerHTML = renderProductDetail();
                    break;
                case 'cart':
                    appEl.innerHTML = renderCart();
                    break;
                case 'orders':
                    appEl.innerHTML = renderOrders();
                    break;
                case 'wallet':
                    appEl.innerHTML = renderWallet();
                    break;
                case 'profile':
                    appEl.innerHTML = renderProfile();
                    break;
                case 'create-store':
                    appEl.innerHTML = renderStoreCreation();
                    break;
                case 'checkout':
                    appEl.innerHTML = renderCheckout();
                    break;
                default:
                    appEl.innerHTML = renderDashboard();
            }
            
            setupEventListeners();
        }
        
        // Dashboard screen
        function renderDashboard() {
            return `
                <!-- Dashboard Header -->
                <header class="p-4">
                    <div class="flex justify-between items-center">
                        <div>
                            <h1 class="text-2xl font-bold">Welcome, ${appState.user.name}!</h1>
                            <p class="text-gray-400 text-sm">Your dropshipping journey starts here</p>
                        </div>
                        <img src="https://picsum.photos/100/100?random=avatar" alt="User Avatar" class="w-12 h-12 rounded-full">
                    </div>
                </header>
                
                <!-- Stats Overview -->
                <div class="px-4 py-2">
                    <div class="grid grid-cols-2 gap-3">
                        <div class="bg-indigo-900/50 rounded-xl p-4">
                            <div class="flex items-center justify-between">
                                <div>
                                    <p class="text-gray-400 text-sm">Your Balance</p>
                                    <h3 class="text-xl font-bold">${(appState.user.balance).toLocaleString()} ₽</h3>
                                </div>
                                <div class="w-12 h-12 rounded-full bg-indigo-700 flex items-center justify-center">
                                    <i class="fas fa-ruble-sign text-white text-xl"></i>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-purple-900/50 rounded-xl p-4">
                            <div class="flex items-center justify-between">
                                <div>
                                    <p class="text-gray-400 text-sm">DropCoin</p>
                                    <h3 class="text-xl font-bold">${appState.user.cryptoBalance.toFixed(2)} DRP</h3>
                                </div>
                                <div class="w-12 h-12 rounded-full bg-purple-700 flex items-center justify-center">
                                    <i class="fas fa-coins text-white text-xl"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Action Cards -->
                <div class="p-4">
                    <h2 class="text-lg font-bold mb-3">Quick Actions</h2>
                    <div class="grid grid-cols-3 gap-3">
                        <button data-navigate="store" class="bg-gray-800/50 rounded-xl p-3 text-center">
                            <div class="w-12 h-12 mx-auto mb-2 rounded-full bg-blue-600 flex items-center justify-center">
                                <i class="fas fa-store text-white text-xl"></i>
                            </div>
                            <p class="text-sm">My Store</p>
                        </button>
                        
                        <button data-navigate="wallet" class="bg-gray-800/50 rounded-xl p-3 text-center">
                            <div class="w-12 h-12 mx-auto mb-2 rounded-full bg-indigo-600 flex items-center justify-center">
                                <i class="fas fa-wallet text-white text-xl"></i>
                            </div>
                            <p class="text-sm">Wallet</p>
                        </button>
                        
                        <button id="view-quests" class="bg-gray-800/50 rounded-xl p-3 text-center">
                            <div class="w-12 h-12 mx-auto mb-2 rounded-full bg-green-600 flex items-center justify-center">
                                <i class="fas fa-coins text-white text-xl"></i>
                            </div>
                            <p class="text-sm">Earn DRP</p>
                        </button>
                    </div>
                </div>
                
                <!-- NFTs Section -->
                <div class="p-4">
                    <div class="flex justify-between items-center mb-3">
                        <h2 class="text-lg font-bold">Your NFTs</h2>
                        <button id="view-all-nfts" class="text-indigo-400 font-medium text-sm">View All</button>
                    </div>
                    
                    <div class="flex space-x-4 overflow-x-auto pb-2 scrollbar-hide">
                        ${appState.nfts.slice(0, 3).map(nft => `
                            <div class="nft-card flex-shrink-0 w-40 rounded-2xl overflow-hidden">
                                <div class="relative">
                                    <img src="${nft.image}" alt="${nft.title}" class="w-full h-32 object-cover">
                                    <div class="absolute top-2 right-2 bg-indigo-600 text-white text-xs px-2 py-1 rounded-full">
                                        NFT
                                    </div>
                                </div>
                                <div class="p-3">
                                    <h3 class="font-bold truncate">${nft.title}</h3>
                                    <p class="text-xs text-gray-400">${nft.collection}</p>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                
                <!-- Quest Section -->
                <div class="p-4">
                    <div class="flex justify-between items-center mb-3">
                        <h2 class="text-lg font-bold">Crypto Quests</h2>
                        <button id="view-quests" class="text-indigo-400 font-medium text-sm">View All</button>
                    </div>
                    
                    <div class="space-y-3">
                        ${appState.quests.slice(0, 2).map(quest => `
                            <div class="bg-gray-800/50 rounded-xl p-4">
                                <div class="flex items-center justify-between">
                                    <h3 class="font-medium">${quest.title}</h3>
                                    <span class="bg-green-600/20 text-green-400 text-xs px-2 py-1 rounded-full">
                                        +${quest.reward} DRP
                                    </span>
                                </div>
                                <div class="mt-2">
                                    <div class="w-full bg-gray-700 rounded-full h-1.5">
                                        <div class="${quest.completed ? 'w-full' : 'w-1/3'} bg-indigo-500 h-1.5 rounded-full"></div>
                                    </div>
                                    <div class="flex justify-between mt-1 text-xs text-gray-400">
                                        <span>${quest.completed ? 'Completed' : 'In Progress'}</span>
                                        <span>${quest.completed ? '100%' : '33%'}</span>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                
                <!-- Marketplace Promo -->
                <div class="p-4">
                    <div class="bg-gradient-to-r from-indigo-900 to-purple-900 rounded-2xl overflow-hidden">
                        <div class="p-5">
                            <div class="flex items-center justify-between mb-3">
                                <div>
                                    <h2 class="text-xl font-bold mb-1">DropFlow Market</h2>
                                    <p class="text-sm text-indigo-200">Shop with crypto & get exclusive NFTs</p>
                                </div>
                                <div class="w-14 h-14 rounded-full bg-purple-700/30 flex items-center justify-center">
                                    <i class="fas fa-shopping-bag text-white text-2xl"></i>
                                </div>
                            </div>
                            <button 
                                id="explore-market"
                                class="w-full bg-white text-indigo-900 font-bold py-2.5 px-4 rounded-lg transition duration-300"
                            >
                                Explore Now
                            </button>
                        </div>
                    </div>
                </div>
                
                <!-- Navigation -->
                ${renderNavBar('dashboard')}
            `;
        }
        
        // Marketplace screen
        function renderMarketplace() {
            const filteredProducts = appState.selectedCategory === "All" 
                ? appState.products 
                : appState.products.filter(p => p.category === appState.selectedCategory);
            
            return `
                <!-- Marketplace Header -->
                <header class="sticky top-0 z-10 bg-gray-900 border-b border-gray-800 px-4 py-3">
                    <div class="flex justify-between items-center">
                        <button data-navigate="dashboard">
                            <i class="fas fa-arrow-left text-xl"></i>
                        </button>
                        <h1 class="text-xl font-bold">DropFlow Market</h1>
                        <div class="flex items-center gap-4">
                            <button class="relative" data-navigate="cart">
                                <i class="fas fa-shopping-cart text-xl"></i>
                                ${getCartItemCount() > 0 ? `
                                    <span class="absolute -top-1 -right-1 w-5 h-5 rounded-full bg-red-500 text-white text-xs flex items-center justify-center">
                                        ${getCartItemCount()}
                                    </span>
                                ` : ''}
                            </button>
                        </div>
                    </div>
                    
                    <!-- Categories -->
                    <div class="flex overflow-x-auto gap-3 mt-4 pb-2 scrollbar-hide">
                        ${appState.categories.map(category => `
                            <button 
                                data-category="${category}"
                                class="px-4 py-2 rounded-full whitespace-nowrap flex-shrink-0 text-sm
                                ${appState.selectedCategory === category ? 'gradient-bg text-white font-medium' : 'bg-gray-800 hover:bg-gray-700'}"
                            >
                                ${category}
                            </button>
                        `).join('')}
                    </div>
                </header>
                
                <!-- Marketplace Content -->
                <main class="p-4 pb-20">
                    <!-- Search Bar -->
                    <div class="relative mb-4">
                        <input 
                            type="text" 
                            placeholder="Search for products..."
                            class="w-full bg-gray-800 border border-gray-700 rounded-xl py-3 px-4 pl-11 focus:outline-none focus:ring-1 focus:ring-indigo-500"
                        >
                        <i class="fas fa-search absolute left-4 top-3.5 text-gray-400"></i>
                    </div>
                    
                    <!-- Featured Products -->
                    <div class="grid grid-cols-2 gap-4">
                        ${filteredProducts.map(product => `
                            <div 
                                class="bg-gray-800/50 border border-gray-700 rounded-xl overflow-hidden transition-transform hover:scale-[1.02]"
                                data-product-id="${product.id}"
                            >
                                <div class="relative pt-[100%]">
                                    <img src="${product.image}" alt="${product.name}" class="absolute top-0 left-0 w-full h-full object-cover">
                                    <div class="absolute bottom-2 right-2 bg-black/40 backdrop-blur-sm px-2 py-1 rounded-full text-white text-xs">
                                        ${product.stock} left
                                    </div>
                                </div>
                                <div class="p-3">
                                    <div class="flex items-start justify-between">
                                        <div class="flex-1 pr-2">
                                            <h3 class="font-medium text-sm line-clamp-1">${product.name}</h3>
                                            <p class="text-xs text-gray-400">${product.store}</p>
                                        </div>
                                        <button 
                                            class="w-7 h-7 rounded-full bg-indigo-600 hover:bg-indigo-700 flex items-center justify-center"
                                            data-add-to-cart="${product.id}"
                                        >
                                            <i class="fas fa-plus text-xs text-white"></i>
                                        </button>
                                    </div>
                                    <div class="mt-2">
                                        <p class="font-bold">${(product.price).toLocaleString()} ₽</p>
                                        <p class="text-xs text-indigo-400">${product.cryptoPrice.toFixed(2)} DRP</p>
                                    </div>
                                    <div class="flex items-center mt-2">
                                        <div class="flex text-amber-400 text-xs mr-1">
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star-half-alt"></i>
                                        </div>
                                        <span class="text-xs text-gray-400">${product.rating}</span>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </main>
                
                ${renderNavBar('market')}
            `;
        }
        
        // Store management screen
        function renderStoreManagement() {
            const userStores = appState.stores.filter(store => appState.user.stores.includes(store.id));
            
            return `
                <!-- Store Management Header -->
                <header class="sticky top-0 z-10 bg-gray-900 border-b border-gray-800 px-4 py-3">
                    <div class="flex justify-between items-center">
                        <button data-navigate="dashboard">
                            <i class="fas fa-arrow-left text-xl"></i>
                        </button>
                        <h1 class="text-xl font-bold">Your Stores</h1>
                        <button data-action="open-create-store-modal" class="text-indigo-400 font-medium">
                            Create
                        </button>
                    </div>
                </header>
                
                <main class="p-4 pb-20">
                    ${userStores.length > 0 ? `
                        <div class="space-y-4">
                            ${userStores.map(store => `
                                <div 
                                    class="bg-gray-800/50 border border-gray-700 rounded-xl overflow-hidden"
                                    style="border-left: 4px solid ${store.color};"
                                >
                                    <div class="p-4">
                                        <div class="flex justify-between items-start mb-3">
                                            <div>
                                                <h2 class="font-bold">${store.name}</h2>
                                                <p class="text-xs text-gray-400">${store.category}</p>
                                            </div>
                                            <div class="bg-gray-700 rounded-full py-1 px-3 text-xs">
                                                ${store.sales} Sales
                                            </div>
                                        </div>
                                        
                                        <div class="flex items-center justify-between mt-4">
                                            <div>
                                                <p class="text-xs text-gray-400">Products</p>
                                                <p class="font-bold">${store.products.length}</p>
                                            </div>
                                            <div>
                                                <p class="text-xs text-gray-400">Rating</p>
                                                <div class="flex items-center">
                                                    <i class="fas fa-star text-amber-400 text-xs mr-1"></i>
                                                    <span class="font-bold">${store.rating}</span>
                                                </div>
                                            </div>
                                            <div>
                                                <p class="text-xs text-gray-400">Earnings</p>
                                                <p class="font-bold">${(store.sales * 500).toLocaleString()} ₽</p>
                                            </div>
                                        </div>
                                        
                                        <div class="grid grid-cols-2 gap-2 mt-4">
                                            <button class="bg-gray-700 hover:bg-gray-600 rounded-lg py-2 text-sm transition">
                                                <i class="fas fa-chart-simple mr-1"></i> Stats
                                            </button>
                                            <button class="bg-indigo-600 hover:bg-indigo-700 rounded-lg py-2 text-sm transition">
                                                <i class="fas fa-pen mr-1"></i> Edit
                                            </button>
                                        </div>
                                    </div>
                                    
                                    <div class="border-t border-gray-700 mt-3 p-3">
                                        <h3 class="text-sm font-medium mb-2">Products</h3>
                                        <div class="grid grid-cols-3 gap-2">
                                            ${appState.products
                                                .filter(p => p.store === store.name)
                                                .slice(0, 3)
                                                .map(product => `
                                                    <div class="bg-gray-700 rounded-lg overflow-hidden">
                                                        <div class="relative pt-[100%]">
                                                            <img src="${product.image}" alt="${product.name}" class="absolute top-0 left-0 w-full h-full object-cover">
                                                        </div>
                                                    </div>
                                                `).join('')
                                            }
                                            <button class="bg-gray-700 hover:bg-gray-600 rounded-lg flex items-center justify-center">
                                                <i class="fas fa-plus text-xl text-gray-400"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    ` : `
                        <div class="text-center py-10">
                            <div class="w-24 h-24 rounded-full bg-indigo-900/20 mx-auto mb-6 flex items-center justify-center">
                                <i class="fas fa-store text-indigo-500 text-4xl"></i>
                            </div>
                            <h2 class="text-xl font-bold mb-2">No Stores Yet</h2>
                            <p class="text-gray-400 mb-6">Create your first store and start your dropshipping journey</p>
                            <button 
                                data-action="open-create-store-modal"
                                class="gradient-bg px-6 py-3 rounded-lg text-white font-medium"
                            >
                                Create Store <i class="fas fa-plus ml-1"></i>
                            </button>
                        </div>
                    `}
                </main>
            `;
        }
        
        function setupEventListeners() {
            // Navigation buttons
            document.querySelectorAll('[data-navigate]').forEach(btn => {
                btn.addEventListener('click', () => {
                    navigate(btn.getAttribute('data-navigate'));
                });
            });
            
            // Create store modal
            document.querySelectorAll('[data-action="open-create-store-modal"]').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.getElementById('store-creation-modal').classList.remove('hidden');
                    setTimeout(() => {
                        document.querySelector('#store-creation-modal > div').classList.add('opacity-100', 'scale-100');
                    }, 10);
                });
            });
            
            // Modal close buttons
            document.getElementById('close-store-modal')?.addEventListener('click', () => {
                document.querySelector('#store-creation-modal > div').classList.remove('opacity-100', 'scale-100');
                setTimeout(() => {
                    document.getElementById('store-creation-modal').classList.add('hidden');
                }, 300);
            });
            
            // NFT Collection view
            document.getElementById('view-all-nfts')?.addEventListener('click', () => {
                document.getElementById('nft-modal').classList.remove('hidden');
            });
            
            // Close NFT modal
            document.getElementById('close-nft-modal')?.addEventListener('click', () => {
                document.getElementById('nft-modal').classList.add('hidden');
            });
            
            // View quests
            document.getElementById('view-quests')?.addEventListener('click', () => {
                document.getElementById('quests-modal').classList.remove('hidden');
            });
            
            // Close quests modal
            document.getElementById('close-quests-modal')?.addEventListener('click', () => {
                document.getElementById('quests-modal').classList.add('hidden');
            });
            
            // Explore market
            document.getElementById('explore-market')?.addEventListener('click', () => {
                navigate('market');
            });
            
            // Create store button
            document.getElementById('create-store-btn')?.addEventListener('click', () => {
                const storeName = document.getElementById('store-name').value;
                const category = document.getElementById('store-category').value;
                
                if (storeName && category) {
                    // Close modal
                    document.querySelector('#store-creation-modal > div').classList.remove('opacity-100', 'scale-100');
                    setTimeout(() => {
                        document.getElementById('store-creation-modal').classList.add('hidden');
                    }, 300);
                    
                    // Create store logic
                    const newStore = {
                        id: appState.stores.length + 1,
                        name: storeName,
                        category,
                        owner: appState.user.id,
                        products: [],
                        rating: 4.5,
                        sales: 0,
                        color: "#4f46e5",
                        created: new Date().toISOString().split('T')[0]
                    };
                    
                    appState.stores.push(newStore);
                    appState.user.stores.push(newStore.id);
                    
                    // Notify
                    alert(`Store "${storeName}" created successfully!`);
                    navigate('store');
                } else {
                    alert('Please fill in all fields');
                }
            });
        }
        
        // Initialize the app
        initializeSampleData();
        renderApp();
        
        // Listen for theme changes
        tg.onEvent('themeChanged', () => {
            if (tg.themeParams) {
                document.documentElement.style.setProperty('--tg-theme-bg-color', tg.themeParams.bg_color || '#0f172a');
                document.documentElement.style.setProperty('--tg-theme-text-color', tg.themeParams.text_color || '#f8fafc');
                document.documentElement.style.setProperty('--tg-theme-hint-color', tg.themeParams.hint_color || '#94a3b8');
                document.documentElement.style.setProperty('--tg-theme-link-color', tg.themeParams.link_color || '#60a5fa');
                document.documentElement.style.setProperty('--tg-theme-button-color', tg.themeParams.button_color || '#4f46e5');
                document.documentElement.style.setProperty('--tg-theme-button-text-color', tg.themeParams.button_text_color || '#ffffff');
            }
        });
    </script>
</body>
</html>
